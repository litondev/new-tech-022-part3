from tokenize import String
from wtforms import Form,StringField,validators

class ProfilUpdatePasswordValidation(Form):
    password = StringField('Password',[
		validators.DataRequired()
	])

    password_confirmation = StringField('Password Confirmation',[
        validators.DataRequired()
    ])
    