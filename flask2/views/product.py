from crypt import methods
from app import app
from middlewares import is_login
from flask import jsonify,make_response, request

class Product:
   @app.route("/product",methods=["GET"])
   @is_login
   def product_index(jwt_decode):
       return "Index"
    
   @app.route("/product",methods=["POST"])
   @is_login
   def product_store(jwt_decode):
       return "Store"
    
   @app.route("/product/<id>",methods=["GET"])
   @is_login
   def product_show(id,**args):
       print(id)
       print(args["jwt_decode"])
       return "Show"

   @app.route("/product/<id>",methods=["PUT"])
   @is_login
   def product_update(id,**args):
       print(id)
       print(args["jwt_decode"])
       return "Update"

   @app.route("/product/<id>",methods=["DELETE"])
   @is_login
   def product_update(id,**args):
       print(id)
       print(args["jwt_decode"])
       return "DELETE"