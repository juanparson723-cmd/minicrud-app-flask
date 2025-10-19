from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class AlumnoForm(FlaskForm):
    matricula = StringField('Matrícula', validators=[DataRequired()])
    nombre = StringField('Nombre', validators=[DataRequired()])
    grupo = StringField('Grupo', validators=[DataRequired()])
    submit = SubmitField('Guardar')
