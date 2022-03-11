from wtforms import Form,StringField,validators

class SigninValidation(Form):
	email = StringField('Email',[
		validators.Length(min=6,max=35),
		validators.Email()
	])

	password = StringField('Password',[
		validators.DataRequired()
	])