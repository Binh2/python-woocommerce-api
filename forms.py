from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField, IntegerField, BooleanField,
           RadioField, FloatField)
from wtforms.validators import InputRequired, Length


class ProductForm(FlaskForm):
  name = StringField('Name')
  price = FloatField('Price')
  brand = StringField('Brand')
  description = TextAreaField('Description')
  images = StringField('Images')
  # weight = FloatField('Weight(kg)')
  # length = FloatField('Length(cm)')
  # width = FloatField('Width(cm)')
  # height = FloatField('Height(cm)')