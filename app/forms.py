from flask_wtf import FlaskForm
from wtforms import HiddenField, StringField, SubmitField
from wtforms.validators import DataRequired


class AnswerForm(FlaskForm):
    answer = StringField('Answer', validators=[DataRequired()], render_kw={"placeholder": "Answer"})
    original = HiddenField()
    submit = SubmitField('Submit')
