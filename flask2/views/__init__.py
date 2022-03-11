from views.auth import Auth
from views.profil import Profil

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