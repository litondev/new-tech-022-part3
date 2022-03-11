from app import app
from middlewares import is_login
from flask import jsonify,make_response, request
from models import User
import bcrypt
from main import db
from validators.profil_update_data_validator import ProfilUpdateDataValidation
from validators.profil_update_password_validator import ProfilUpdatePasswordValidation
from werkzeug.utils import secure_filename
import os
import string
import random

class Profil:
    @app.route("/profil/data",methods=["POST"])
    @is_login
    def profil_data(jwt_decode):
        try:
            form = ProfilUpdateDataValidation(request.form)

            if not form.validate():
                return make_response(jsonify({
                    "message" : form.errors[list(form.errors.keys())[0]][0]
                }),422)

            user_email = User.query.filter(
                User.email == request.form['email'],
                User.id != jwt_decode['sub']
            ).count();
            
            if(user_email > 0):
                return make_response(jsonify({
                    "message" : "Email telah terpakai"
                }),422)

            user = User.query.filter_by(id=jwt_decode['sub']).first()

            if(bcrypt.checkpw(bytes(request.form['password'].encode("utf-8")),bytes(user.password.encode("utf-8"))) == False):
                return make_response(jsonify({"message" : "Password tidak valid"}),422)                                
                    
            user.name = request.form["name"]
            user.email = request.form["email"]

            db.session.commit() 

            return make_response(jsonify({"message" : True}), 200)
        except Exception as e:    
            db.session.rollback() 
            
            print(e)

            app.logger.warning(e)

            return make_response(jsonify({"message" : "Terjadi Kesalahan"}),500)   
    
    @app.route("/profil/password",methods=["POST"])
    @is_login
    def profil_password(jwt_decode):
        try:
            form = ProfilUpdatePasswordValidation(request.form)

            if not form.validate():
                return make_response(jsonify({
                    "message" : form.errors[list(form.errors.keys())[0]][0]
                }),422)
          
            user = User.query.filter_by(id=jwt_decode['sub']).first()

            if(bcrypt.checkpw(bytes(request.form['password_confirmation'].encode("utf-8")),bytes(user.password.encode("utf-8"))) == False):
                return make_response(jsonify({"message" : "Password tidak valid"}),422)                                
                    
            user.password = bcrypt.hashpw(bytes(request.form['password'].encode("utf-8")), bcrypt.gensalt())

            db.session.commit() 

            return make_response(jsonify({"message" : True}), 200)
        except Exception as e:    
            db.session.rollback() 
            
            print(e)

            app.logger.warning(e)

            return make_response(jsonify({"message" : "Terjadi Kesalahan"}),500)   
    
    @staticmethod
    def allowed_file(filename):
        return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg'}

    @app.route("/profil/photo",methods=["POST"])
    @is_login
    def profil_photo(jwt_decode):
        try:
         if 'photo' not in request.files:
            return make_response(jsonify({"message" : "File Does Exist"}),422)

         file = request.files['photo']
         
         if file is None:
            return make_response(jsonify({"message" : "File tidak ditemukan"}),422)

         if Profil.allowed_file(file.filename) == False:
            return make_response(jsonify({"message" : "File tidak diperbolehkan"}),422)
            
         if(file.content_type == "image/png"):
            filename = ''.join(random.choice(string.ascii_lowercase) for i in range(10)) + ".png"
         elif(file.content_type == "image/jpeg"):
            filename = ''.join(random.choice(string.ascii_lowercase) for i in range(10)) + ".jpeg"
         else:
            filename = ''.join(random.choice(string.ascii_lowercase) for i in range(10)) + ".jpg"

         file.save(os.path.join("./static",filename) ) 

         user = User.query.filter_by(id=jwt_decode['sub']).first()       

         if os.path.exists("./static/" + user.photo) and user.photo != "default.png":
           os.remove("./static/" + user.photo)

         user.photo = filename;

         db.session.commit() 

         return make_response(jsonify({"message" : True}))
        except Exception as e:
          db.session.rollback() 

          print(e)

          app.logger.warning(e)

          return make_response(jsonify({"message" : "Terjadi Kesalahan"}),500)   