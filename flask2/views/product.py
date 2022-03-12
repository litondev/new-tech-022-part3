from crypt import methods
import json
from app import app
from middlewares import is_login
from flask import jsonify,make_response, request
from main import db
from models import Product as ProductModel
from validators.product_validator import ProductValidation

class Product:
   @app.route("/product",methods=["GET"])
   @is_login
   def product_index(jwt_decode):
       return "Index"
    
   @app.route("/product",methods=["POST"])
   @is_login
   def product_store(jwt_decode):
        try:
            form = ProductValidation(request.form)

            if not form.validate():
                return make_response(jsonify({
                    "message" : form.errors[list(form.errors.keys())[0]][0]
                }),422)

            
            db.session.add(ProductModel(
                form.title.data,        
                form.stock.data,
                form.price.data,                
                form.description.data
            ))

            db.session.commit() 

            return make_response(jsonify({"message" : True}), 200)
        except Exception as e:    
            db.session.rollback() 
            
            print(e)

            app.logger.warning(e)

            return make_response(jsonify({"message" : "Terjadi Kesalahan"}),500)  
    
   @app.route("/product/<int:id>",methods=["GET"])
   @is_login
   def product_show(id,**args):    
       product = ProductModel.query.filter_by(id=id).first()

       if product == None:
           return make_response(jsonify({"message" : "Not Found"}),404)

       return make_response(jsonify(product.as_dict()))

   @app.route("/product/<int:id>",methods=["PUT"])
   @is_login
   def product_update(id,**args):
        try:
            product = ProductModel.query.filter_by(id=id).first()

            if product == None:
                return make_response(jsonify({"message" : "Not Found"}),404)

            form = ProductValidation(request.form)

            if not form.validate():
                return make_response(jsonify({
                    "message" : form.errors[list(form.errors.keys())[0]][0]
                }),422)
           
            product.title = form.title.data
            product.stock = form.stock.data
            product.price = form.price.data
            product.description = form.description.data

            db.session.commit() 

            return make_response(jsonify({"message" : True}), 200)
        except Exception as e:    
            db.session.rollback() 
            
            print(e)

            app.logger.warning(e)

            return make_response(jsonify({"message" : "Terjadi Kesalahan"}),500) 

   @app.route("/product/<int:id>",methods=["DELETE"])
   @is_login
   def product_delete(id,**args):
        try:
            product = ProductModel.query.filter_by(id=id).first()

            if product == None:
                return make_response(jsonify({"message" : "Not Found"}),400)
                
            ProductModel.query.filter_by(id=id).delete()      

            db.session.commit() 

            return make_response(jsonify({"message" : True}), 200)
        except Exception as e:    
            db.session.rollback() 
            
            print(e)

            app.logger.warning(e)

            return make_response(jsonify({"message" : "Terjadi Kesalahan"}),500) 