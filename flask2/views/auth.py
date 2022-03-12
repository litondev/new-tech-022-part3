from app import app
from validators.signin_validator import SigninValidation
from validators.signup_validator import SignupValidation
from validators.forgot_password_validator import ForgotPasswordValidation
from validators.reset_password_validator import ResetPasswordValidation
from models import User
from flask import jsonify,make_response, request
from main import db
import bcrypt
import datetime 
import jwt 
from middlewares import is_login
from werkzeug.datastructures import ImmutableMultiDict

class Auth:
    @app.route("/signin",methods=["POST"])
    def auth_signin():
        try:
            if not request.is_json:
                form = SigninValidation(request.form)
            else: 
                form = SigninValidation(ImmutableMultiDict(request.get_json()))

            if not form.validate():
                return make_response(jsonify({
                    "message" : form.errors[list(form.errors.keys())[0]][0]
                }),422)

            user = User.query.filter_by(email=form.email.data).first()
            
            if user == None:
                return make_response(jsonify({"message" : "Email tidak ditemukan"}),422)

            if(bcrypt.checkpw(bytes(form.password.data.encode("utf-8")),bytes(user.password.encode("utf-8"))) == False):
                return make_response(jsonify({"message" : "Password tidak valid"}),422)
                    
            
            token = jwt.encode({
                'sub' : user.id, 
                'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=45)
            },app.config['SECRET_KEY'], "HS256")             
        
            return make_response(jsonify({
                "message" : True,
                "user" : user.as_dict(),
                "token" : token.decode("utf-8")
            }), 200)
        except Exception as e:            
            print(e)

            app.logger.warning(e)

            return make_response(jsonify({"message" : "Terjadi Kesalahan"}),500)  
    
    @app.route("/signup",methods=["POST"])
    def auth_signup():
        try:
            form = SignupValidation(request.form)

            if not form.validate():
                return make_response(jsonify({
                    "message" : form.errors[list(form.errors.keys())[0]][0]
                }),422)


            salt = bcrypt.gensalt()

            hashed = bcrypt.hashpw(bytes(request.form['password'].encode("utf-8")), salt)

            db.session.add(User(request.form['name'],request.form['email'],hashed))

            db.session.commit() 

            return make_response(jsonify({"message" : True}), 200)
        except Exception as e:
            db.session.rollback()

            print(e)

            app.logger.warning(e)

            return make_response(jsonify({"message" : "Terjadi Kesalahan"}),500)            


    @app.route("/forgot-password",methods=["POST"])
    def auth_forgot_password():
        try:
            form = ForgotPasswordValidation(request.form)

            if not form.validate():
                return make_response(jsonify({
                    "message" : form.errors[list(form.errors.keys())[0]][0]
                }),422)

            user = User.query.filter_by(email=request.form['email']).first()
            
            if user == None:
                return make_response(jsonify({"message" : "Email tidak ditemukan"}),422)
            
            user.remember_token = "12345";

            db.session.commit() 

            return make_response(jsonify({"message" : True}), 200)
        except Exception as e:    
            db.session.rollback() 
            
            print(e)

            app.logger.warning(e)

            return make_response(jsonify({"message" : "Terjadi Kesalahan"}),500)    

    @app.route("/reset-password",methods=["POST"])
    def auth_reset_password():
        try:
            form = ResetPasswordValidation(request.form)

            if not form.validate():
                return make_response(jsonify({
                    "message" : form.errors[list(form.errors.keys())[0]][0]
                }),422)

            user = User.query.filter_by(email=request.form['email']).first()
            
            if user == None:
                return make_response(jsonify({"message" : "Email tidak ditemukan"}),422)
            
            if(user.remember_token != request.form['token']):
                return make_response(jsonify({"message" : "Token tidak valid"}),422)

            if(request.form['password'] != request.form['password_confirmation']):
                return make_response(jsonify({"message" : "Password tidak sama"}),422)

            salt = bcrypt.gensalt()

            hashed = bcrypt.hashpw(bytes(request.form['password'].encode("utf-8")), salt)

            user.password = hashed;

            db.session.commit() 

            return make_response(jsonify({"message" : True}), 200)
        except Exception as e:    
            db.session.rollback() 
            
            print(e)

            app.logger.warning(e)

            return make_response(jsonify({"message" : "Terjadi Kesalahan"}),500)   
    
    @app.route("/me",methods=["GET"])
    @is_login	
    def auth_me(jwt_decode):
        print(jwt_decode)
        user = User.query.filter_by(id=jwt_decode['sub']).first()
        return make_response(jsonify(user.as_dict()), 200)

    @app.route("/logout",methods=["POST"])
    def auth_logout():
        return make_response(jsonify({"message" : True}), 200)
    