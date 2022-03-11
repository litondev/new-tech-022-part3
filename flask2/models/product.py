from main import db
from sqlalchemy.sql import func

class Product(db.Model):
    id = db.Column(
            db.Integer, 
            autoincrement=True, 
            primary_key=True
        )

    title = db.Column(
            db.String(50),
            nullable=False
        )

    stock = db.Column(
        db.Integer,
        default=0
    )

    price = db.Column(
        db.Float,
        default=0.00
    )

    description = db.Column(
        db.Text,
        nullable=True,
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
    
    def __init__(self,title,stock,price,description):
      self.title = title
      self.stock = stock
      self.price = price 
      self.description = description
 
    def __repr__(self):     
      return '<Product title={self.title} stock={self.stock} price={self.price} description={self.description}>'