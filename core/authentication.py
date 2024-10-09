import datetime
from jwt import JWT, jwk_from_dict
from jwt.utils import get_int_from_datetime
from rest_framework import exceptions

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
