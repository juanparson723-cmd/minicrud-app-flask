from flask import render_template, request, redirect, url_for
from app import app, db
from models import Alumno
from form import AlumnoForm

@app.route('/')
def index():
    alumnos = Alumno.query.all()
    return render_template('index.html', alumnos=alumnos)

@app.route('/crear', methods=['GET', 'POST'])
def crear():
    form = AlumnoForm()
    if form.validate_on_submit():
        alumno = Alumno(matricula=form.matricula.data, nombre=form.nombre.data, grupo=form.grupo.data)
        db.session.add(alumno)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('crear.html', form=form)

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    alumno = Alumno.query.get_or_404(id)
    form = AlumnoForm(obj=alumno)
    if form.validate_on_submit():
        alumno.matricula = form.matricula.data
        alumno.nombre = form.nombre.data
        alumno.grupo = form.grupo.data
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('editar.html', form=form, alumno=alumno)

@app.route('/borrar/<int:id>')
def borrar(id):
    alumno = Alumno.query.get_or_404(id)
    db.session.delete(alumno)
    db.session.commit()
    return redirect(url_for('index'))
