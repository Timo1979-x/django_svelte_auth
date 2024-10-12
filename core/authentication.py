import datetime
from jwt import JWT, jwk_from_dict
from jwt.utils import get_int_from_datetime
from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication, get_authorization_header
from .models import User

access_signing_key = jwk_from_dict({'kty': 'oct', 'k': 'YWNjZXNzX3NlY3JldAo='}) # 'access_secret'
refresh_signing_key = jwk_from_dict({'kty': 'oct', 'k': 'cmVmcmVzaF9zZWNyZXQK'}) # 'refresh_secret'

def create_token(id, key, delta):
  now = datetime.datetime.now(datetime.timezone.utc)
  return JWT().encode(
    {
      'user_id': id,
      'exp': get_int_from_datetime(now + delta),
      'iat': get_int_from_datetime(now),
    },
    key,
    alg = 'HS256'
  )

class JWTAuthentication(BaseAuthentication):
  def authenticate(self, request):
    auth = get_authorization_header(request).split()
    if auth and len(auth) == 2:
      token = auth[1].decode('utf-8')
      id = decode_access_token(token)
      user = User.objects.get(pk = id)
      return (user, None)
    raise exceptions.AuthenticationFailed('unauthenticated2')
  
def create_access_token(id):
  return create_token(id, access_signing_key, datetime.timedelta(seconds = 30))

def decode_access_token(token):
  try:
    payload = JWT().decode(token, access_signing_key)
    return payload['user_id']
  except Exception as e:
    print(e)
    raise exceptions.AuthenticationFailed('unauthenticated1')

def create_refresh_token(id):
  return create_token(id, refresh_signing_key, datetime.timedelta(days = 7))
