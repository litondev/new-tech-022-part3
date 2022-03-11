from views.auth import Auth
from views.profil import Profil
from views.product import Product

user_web_auth = Auth()
"""
 - /signin (POST)
 - /signup (POST)
 - /forgot-password (POST)
 - /reset-password (POST)
 - /logout (POST)
 - /me (GET)
"""

user_web_profil = Profil()
"""
 - /profil/data (POST)
 - /profil/password (POST)
 - /profil/photo (POST)
"""

user_web_product = Product()
""""
 - /product (GET)
 - /product/show/:id (GET)
 - /product/store (POST)
 - /product/update/:id (PUT)
 - /product/destroy/:id (DELETE)
"""