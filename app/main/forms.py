from unicodedata import category
from flask_wtf import FlaskForm
from wtforms import TextAreaField,SelectField,SubmitField

from wtforms.validators import InputRequired

class PitchForm(FlaskForm):
  pitch=TextAreaField('',validators=[InputRequired()],render_kw={"placeholder": "Pitch away.."})
  category=SelectField('Category',choices=[('pickup_lines','Pickup Line'),('product_pitch','Product Pitch'),('promotional_pitch','Promotional Pitch'),('interview','Interview')],validators=[InputRequired()])
  submit=SubmitField('Submit')