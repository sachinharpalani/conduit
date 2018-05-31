import jwt
from django.conf.global_settings import SECRET_KEY

def get_token(payload):
    token = jwt.encode(payload,SECRET_KEY,algorithm='HS256')
    return str(token,'utf-8')

def get_payload(token):
    payload = jwt.decode(token,SECRET_KEY,algorihms=['HS256'])
    return payload
