from wtforms import Form,StringField,validators

class ForgotPasswordValidation(Form):
	email = StringField('Email',[
		validators.Length(min=6,max=35),
		validators.Email()
	])