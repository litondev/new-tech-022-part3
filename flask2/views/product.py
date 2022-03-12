from crypt import methods
import json

from sqlalchemy import desc
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
       page = request.args.get("page") or 1
       search = request.args.get("search") 

       if search != None :
         last_id_search = ProductModel.query.filter(
           ProductModel.title.ilike('%'+search+"%")
         ).order_by(
            ProductModel.id.desc()
         ).first()

         total_products = last_id_search.id;
                 
         if(int(page) == 1 or int(page) == 0):
            current_page = (int(total_products)) + 1
         else:
            current_page = (int(total_products) - ((int(page)-1)*10))

         products = ProductModel.query.filter(
            ProductModel.id <= current_page,
            ProductModel.title.ilike('%'+search+"%")
         ).order_by(
            ProductModel.id.desc()
         ).limit(10).all()

         return make_response(jsonify({
            "page" : page,
            "data" : [p.as_dict() for p in products]
         }))
       else:
        total_products = ProductModel.query.count();

        if(int(page) == 1 or int(page) == 0):
            current_page = (int(total_products)) + 1
        else:
            current_page = (int(total_products) - ((int(page)-1)*10))

        products = ProductModel.query.filter(
            ProductModel.id <= current_page 
        ).order_by(
            ProductModel.id.desc()
        ).limit(10).all()

        return make_response(jsonify({
            "page" : page,
            "data" : [ p.as_dict() for p in products ],
        }))
    
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