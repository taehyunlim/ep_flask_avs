from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, FloatField,  SelectField
from wtforms.validators import DataRequired, ValidationError, Length, NumberRange, Optional

class AddressForm(FlaskForm):
  name = StringField('Name', validators=[DataRequired()])
  street1 = StringField('Street 1', validators=[DataRequired(), Length(min=0, max=30)])
  street2 = StringField('Street 2', validators=[Length(min=0, max=30)])
  city = StringField('City', validators=[DataRequired(), Length(min=0, max=30)])
  state = StringField('State', validators=[DataRequired(), Length(min=0, max=2)])
  zip = StringField('Zip', validators=[DataRequired(), Length(min=0, max=10)])
  country = StringField('Country', validators=[DataRequired(), Length(min=0, max=20)])
  verify = SelectField('AVS', validators=[Optional()], choices=[('delivery', 'Delivery'), ('zip4', 'Zip4')])
  submit = SubmitField('Submit')