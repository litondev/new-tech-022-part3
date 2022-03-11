from app import app
from validators.signin_validator import SigninValidation
from validators.signup_validator import SignupValidation
from models import User
from flask import jsonify,make_response, request
from main import db
import bcrypt

class Auth:
    @app.route("/signin",methods=["POST"])
    def auth_signin():
        return make_response(jsonify({"message" : "Signin"}), 200)
    
    @app.route("/signup",methods=["POST"])
    def auth_signup():
        try:
            form = SignupValidation(request.form)

            if not form.validate():
                return make_response(jsonify({
                    "message" : form.errors[list(form.errors.keys())[0]][0]
                }),422)


            salt = bcrypt.gensalt()

            hashed = bcrypt.hashpw(b""+request.form['password']+"", salt)

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
        return make_response(jsonify({"message" : "Forgot Password"}), 200)

    @app.route("/reset-password",methods=["POST"])
    def auth_reset_password():
        return make_response(jsonify({"message" : "Reset Password"}), 200)
    
    @app.route("/me",methods=["GET"])
    def auth_me():
        return make_response(jsonify({"message" : "Me"}), 200)

    @app.route("/logout",methods=["POST"])
    def auth_logout():
        return make_response(jsonify({"message" : "Logout"}), 200)
    