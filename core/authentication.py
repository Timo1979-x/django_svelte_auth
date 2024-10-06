import datetime
from jwt import JWT, jwk_from_dict
from jwt.utils import get_int_from_datetime

access_signing_key = jwk_from_dict({'kty': 'oct', 'k': 'YWNjZXNzX3NlY3JldAo='}) # 'access_secret'
refresh_signing_key = jwk_from_dict({'kty': 'oct', 'k': 'cmVmcmVzaF9zZWNyZXQK'}) # 'refresh_secret'
print(access_signing_key)
print(access_signing_key.get_kty())

def create_access_token(id):
  now = datetime.datetime.now(datetime.timezone.utc)
  return JWT().encode(
    {
      'user_id': id,
      'exp': get_int_from_datetime(now + datetime.timedelta(seconds = 30)),
      'iat': get_int_from_datetime(now),
    },
    access_signing_key,
    alg = 'HS256'
  )

def create_refresh_token(id):
  now = datetime.datetime.now(datetime.timezone.utc)
  return JWT().encode(
    {
      'user_id': id,
      'exp': get_int_from_datetime(now + datetime.timedelta(days = 7)),
      'iat': get_int_from_datetime(now),
    },
    refresh_signing_key,
    alg = 'HS256'
  )
