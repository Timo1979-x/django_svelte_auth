import datetime
import random
import string
import pyotp
from urllib import response
from django.core.mail import send_mail
from django.shortcuts import render
from rest_framework import exceptions
from rest_framework.response import Response
from rest_framework.views import APIView

from .authentication import JWTAuthentication, create_access_token, create_refresh_token, decode_refresh_token

from .models import Reset, User, UserToken
from .serializers import UserSerializer

from google.oauth2 import id_token
from google.auth.transport.requests import Request as GoogleRequest


# Create your views here.
class RegisterAPIView(APIView):
  def post(self, request):
    data = request.data
    if data['password'] != data['password_confirm']:
      raise exceptions.APIException('Passwords dont match!')

    serializer = UserSerializer(data = data)
    serializer.is_valid(raise_exception = True)
    serializer.save()

    return Response(serializer.data)


class LoginAPIView(APIView):
  def post(self, request):
    email = request.data['email']
    password = request.data['password']

    user = User.objects.filter(email = email).first()
    if user is None or not user.check_password(password):
      raise exceptions.AuthenticationFailed('Invalid credentials')

    if user.tfa_secret:
      return Response({
        'id': user.id
      })
    secret = pyotp.random_base32()
    otpauth_url = pyotp.totp.TOTP(secret).provisioning_uri(issuer_name = "My App")
    return Response({
      'id': user.id,
      'secret': secret,
      'otpauth_url': otpauth_url
    })


class TwoFactorAPIView(APIView):
  def post(self, request):
    id = request.data['id']
    user = User.objects.filter(pk = id).first()

    if not user:
      raise exceptions.AuthenticationFailed('Invalid credentials3')
    print("user is {user}".format(user = str(user)))
    secret = user.tfa_secret if user.tfa_secret != '' else request.data['secret']

    if not pyotp.TOTP(secret).verify(request.data['code']):
      raise exceptions.AuthenticationFailed('Invalid credentials4')

    if user.tfa_secret == '':
      print("set new user secret {secret}".format(secret = str(secret)))
      user.tfa_secret = secret
      user.save()

    access_token = create_access_token(id)
    refresh_token = create_refresh_token(id)

    UserToken.objects.create(
      user_id = id,
      token = refresh_token,
      expired_at = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days = 7)
    )

    response = Response()
    response.set_cookie(key = 'refresh_token', value = refresh_token, httponly = True)
    response.data = {
      'token': access_token,
    }
    return response

class UserAPIView(APIView):
  authentication_classes = [JWTAuthentication]
  def get(self, request):
    return Response(UserSerializer(request.user).data)

class RefreshAPIView(APIView):
  def post(self, request):
    refresh_token = request.COOKIES.get('refresh_token')
    id = decode_refresh_token(refresh_token)

    if not UserToken.objects.filter(
      user_id = id,
      token = refresh_token,
      expired_at__gt = datetime.datetime.now(datetime.timezone.utc)
    ).exists():
      raise exceptions.AuthenticationFailed("unauthenticated3")

    access_token = create_access_token(id)
    return Response({
      'token': access_token,
    })

class LogoutAPIView(APIView):
  def post(self, request):
    refresh_token = request.COOKIES.get('refresh_token')
    UserToken.objects.filter(token = refresh_token).delete()

    response = Response()
    response.delete_cookie(key = 'refresh_token')
    response.data = {
      'message': 'success'
    }
    return response

class ForgotAPIView(APIView):
  def post(self, request):
    email = request.data['email']
    token = ''.join(random.choice(string.ascii_lowercase + string.digits + string.ascii_uppercase) for _ in range(10))

    Reset.objects.create(
      email = email,
      token = token
    )


    url = 'http://localhost:8080/#/reset/' + token
    send_mail(
      subject = 'reset password',
      message = 'click <a href="%s">here</a> to reset your password' % url,
      from_email = 'from@example.com',
      recipient_list=[email])

    return Response({
      'message': 'success'
    })

class ResetAPIView(APIView):
  def post(self, request):
    data = request.data
    if data['password'] != data['password_confirm']:
      raise exceptions.APIException('Passwords dont match!')

    reset_password = Reset.objects.filter(token = data['token']).first()

    if not reset_password:
      raise exceptions.APIException('Invalid link!')

    user = User.objects.filter(email = reset_password.email).first()
    if not user:
      raise exceptions.APIException('User not found!')

    user.set_password(data['password'])
    user.save()

    return Response({
      'message': 'success'
    })

class GoogleAuthAPIView(APIView):
  def post(self, request):
    token = request.data['token']
    googleUser = id_token.verify_token(token, GoogleRequest())

    if not googleUser:
      raise exceptions.AuthenticationFailed("unauthenticated G1")
    
    user = User.objects.filter(name = googleUser['email']).first()
    if not user:
      user = User.objects.create(
        first_name = googleUser['given_name'],
        last_name = googleUser['family_name'],
        email = googleUser['email'],
      )
      user.set_password(token)
      user.save()

    id = user.id
    access_token = create_access_token(id)
    refresh_token = create_refresh_token(id)

    UserToken.objects.create(
      user_id = id,
      token = refresh_token,
      expired_at = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days = 7)
    )

    response = Response()
    response.set_cookie(key = 'refresh_token', value = refresh_token, httponly = True)
    response.data = {
      'token': access_token,
    }
    return response
    
