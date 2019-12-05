from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required
from flask_login import current_user 
 
class commentForm(FlaskForm):
    body = TextAreaField('Leave a comment:',validators=[Required()])
    submit = SubmitField('Post comment')
    