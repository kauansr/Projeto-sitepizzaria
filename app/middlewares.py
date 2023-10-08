from functools import wraps
from flask import request, jsonify
import jwt
from app.inicial import app, session
from app.models import User


def token_required(f):

    """
    Decoradora e serve para decordificar o token jwt
    :return: User
    """


    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if "Authentication" in request.headers:
            token =  request.headers["Authentication"]
            
        
        if not token:
            return jsonify({'message': 'nao existe token'}),401
        
        
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            current_user = session.query(User).filter_by(id=data['id']).first()
            current_user.status_log = True
            
            
        except jwt.InvalidTokenError:
            current_user.status_log = False
            return jsonify({'message':'Token e invalido!'})
        
        return f(current_user=current_user, *args, **kwargs)

    return decorated