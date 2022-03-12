from flask import jsonify,make_response, request
from functools import wraps
import jwt 
from app import app

def is_login(f):
    @wraps(f)
    def decorator(*args, **kwargs):
       token = None
       if 'Authorization' in request.headers:
           token = request.headers['Authorization']
 
       if not token:
           return make_response(jsonify({'message': 'Authorization'}),401)
       try:
           jwt_decode = jwt.decode(token.split(" ")[1], app.config['SECRET_KEY'], algorithms=["HS256"])
           kwargs["jwt_decode"] = jwt_decode
           # current_user = Users.query.filter_by(public_id=data['public_id']).first()
       except:
           return make_response(jsonify({'message': 'Authorization'}),401)
 
       return f(*args, **kwargs)
    return decorator