from wtforms import Form,StringField,validators

class ResetPasswordValidation(Form):
    token = StringField('Token',[
		validators.DataRequired()
    ])

    email = StringField('Email',[
		validators.Length(min=6,max=35),
		validators.Email()
	])

    password = StringField('Password',[
		validators.DataRequired()
    ])

    password_confirmation = StringField('Token',[
		validators.DataRequired()
    ])