from email.policy import default
from wtforms import Form,StringField,IntegerField,FloatField,validators

class ProductValidation(Form):
    title = StringField('Title',[
        validators.DataRequired()
    ])

    stock = IntegerField('Stock', [
        validators.DataRequired(message="Stock harus diisi")
    ])    

    price = FloatField('Price',[
        validators.DataRequired()
    ])

    description = StringField('Description',[
        validators.Optional()
    ])