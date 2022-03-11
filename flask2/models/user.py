from main import db
from sqlalchemy.sql import func

class User(db.Model):
    id = db.Column(
            db.Integer, 
            autoincrement=True, 
            primary_key=True
        )

    name = db.Column(
            db.String(50),
            nullable=False
        )
        
    email = db.Column(
            db.String(50),
            nullable=False,
            index=True
        )

    remember_token = db.Column( 
            db.Text,
            nullable=True
    )

    password = db.Column(
            db.Text,
            nullable=False
        )

    photo = db.Column(
            db.String(100),
            default=True,
            server_default="default.png"
        )

    created_at = db.Column(
        db.DateTime(timezone=True),
        nullable=True,
        default=func.now()
    )

    updated_at = db.Column(
        db.DateTime(timezone=True),
        nullable=True,
        default=func.now()
    )
    
    def __init__(self, name, email, password, photo = "default.png"):
      self.name = name
      self.email = email
      self.password = password    
      self.photo = photo
 
    def __repr__(self):     
      return '<User name={self.name} email={self.email}  password={self.password} photo={self.photo} remember_token={self.remember_token}>'