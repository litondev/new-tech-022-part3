from wtforms import Form,StringField,validators

class ProfilUpdateDataValidation(Form):
    name = StringField('name',[
        validators.DataRequired()
    ])

    email = StringField('Email',[
		validators.Length(min=6,max=35),
        validators.Email()
	])
    
    password = StringField('Password',[
		validators.DataRequired()
	])
    