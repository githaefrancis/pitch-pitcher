
from flask_wtf import FlaskForm
from wtforms import TextAreaField,SelectField,SubmitField

from wtforms.validators import InputRequired,DataRequired

class PitchForm(FlaskForm):
  content=TextAreaField('',validators=[],render_kw={"placeholder": "Pitch away.."})
  category=SelectField('Category',choices=[('pickup_lines','Pickup Line'),('product_pitch','Product Pitch'),('promotional_pitch','Promotional Pitch'),('interview','Interview')],validators=[InputRequired()])
  submit=SubmitField('Submit')

class Comment(FlaskForm):
  comment=TextAreaField('',validators=[],render_kw={"placeholder": "Write a comment"})
  submit=SubmitField('Submit')