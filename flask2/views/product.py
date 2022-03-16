from crypt import methods
from sqlalchemy import desc
from app import app
from middlewares import is_login
from flask import jsonify,make_response, request
from main import db
from models import Product as ProductModel
from validators.product_validator import ProductValidation
from werkzeug.datastructures import ImmutableMultiDict

class Product:
   @app.route("/product",methods=["GET"])
   @is_login
   def product_index(jwt_decode):
       page = request.args.get("page") or 1
       search = request.args.get("search") 
        
       ### 
       # * NOTE UNTUK MENGETAHUI LAST PAGE DI FRONTEND CUKUP DENGAN
        # MENGETAHUI DATA KALO PAGENYA KURANG DARI ATAU SAMA DENGAN 10 PASTI 
        # ITU PAGE TERAKHR ATO BISA JUGA DI BANDINGKAN
        # DENGAN PER PAGENYA KALO KURANG DARI ATO SAMA DENGAN PER_PAGENYA PASTI ITU PAGENYA

       if search != None :
         total_products = ProductModel.query.filter( 
                ProductModel.title.ilike('%'+search+"%")
            ).order_by(
                ProductModel.id.desc()
            ).first();

         if(int(page) == 1 or int(page) == 0):
            current_page = total_products.id
         else:
            current_products = ProductModel.query.filter(
                ProductModel.title.ilike('%'+search+"%"),
                ProductModel.id <= page 
            ).order_by(
                ProductModel.id.desc()
            ).first()

            current_page = current_products.id
        
         products = ProductModel.query.filter(
            ProductModel.id <= current_page,
            ProductModel.title.ilike('%'+search+"%")
         ).order_by(
            ProductModel.id.desc()
         ).limit(10).all()

         return make_response(jsonify({
            "first_page" : total_products.id,
            "page" : current_page,
            "data" : [p.as_dict() for p in products]
         }))
       else:                
        total_products = ProductModel.query.order_by(
                ProductModel.id.desc()
            ).first();

        if(int(page) == 1 or int(page) == 0):         
            current_page = total_products.id
        else:
            current_products = ProductModel.query.filter(
                ProductModel.id <= page 
            ).order_by(
                ProductModel.id.desc()
            ).first()

            current_page = current_products.id        

        products = ProductModel.query.filter(
            ProductModel.id <= current_page 
        ).order_by(
            ProductModel.id.desc()
        ).limit(10).all()

        return make_response(jsonify({
            "first_page" : total_products.id,
            "page" : current_page,
            "data" : [ p.as_dict() for p in products ],
        }))
    
   @app.route("/product",methods=["POST"])
   @is_login
   def product_store(jwt_decode):
        try:
            if not request.is_json:
                form = ProductValidation(request.form)
            else: 
                form = ProductValidation(ImmutableMultiDict(request.get_json()))

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

            if not request.is_json:
                form = ProductValidation(request.form)
            else: 
                form = ProductValidation(ImmutableMultiDict(request.get_json()))

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