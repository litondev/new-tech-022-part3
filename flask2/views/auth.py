from app import app
from validators.signin_validator import SigninValidation
from models import User
from flask import jsonify,make_response

class Auth:
	# @app.route("/signin",methods=["POST"])
	# def user_auth_signin_actions():
	# 	form = SigninValidation(request.form)

	# 	if not form.validate():
	# 		flash({
	# 			"status" : "failed",
	# 			"message" : form.errors[list(form.errors.keys())[0]][0]
	# 		})
	# 		return redirect("/")

	# 	user = User.query.filter_by(email=request.form['email']).first()

	# 	if user == None:
	# 		return redirect("/")

	# 	session["user"] = user.id
	# 	return redirect("/user")

    @app.route("/signin",methods=["POST"])
    def auth_signin():
        return make_response(jsonify({"message" : "Signin"}), 200)
    
    @app.route("/signup",methods=["POST"])
    def auth_signup():
        return make_response(jsonify({"message" : "Signup"}), 200)

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
    