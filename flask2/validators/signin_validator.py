from wtforms import Form,StringField,validators

class SigninValidation(Form):
	email = StringField('Email',[
		validators.DataRequired(),
		validators.Length(min=0,max=35),
		validators.Email()
	])

	password = StringField('Password',[
		validators.DataRequired()
	])