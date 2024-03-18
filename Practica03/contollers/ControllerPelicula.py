from flask import Blueprint, request, render_template, flash, redirect, url_for
from sqlalchemy.exc import IntegrityError

from alchemyClasses.Pelicula import Pelicula, db

pelicula_blueprint = Blueprint('pelicula', __name__, url_prefix='/pelicula')

@pelicula_blueprint.route('/', methods=['GET'])
def raiz():
    return render_template('Pelicula/raiz.html')

@pelicula_blueprint.route('/ver_todos', methods=['GET'])
def ver_peliculas():
    peliculas = Pelicula.query.all()
    return render_template('Pelicula/ver_todos.html', peliculas=peliculas)

"""
@pelicula_blueprint.route('/id/<int:id_usuario>/<string:nombre>')
def ver_usuario_id(id_usuario, nombre):
    usuario = Usuario.query.filter_by(idUsuario=id_usuario).first()
    if usuario:
        return f"Nombre: {usuario.nombre}, Email: {usuario.email}"
    else:
        return "Usuario no encontrado"

"""

@pelicula_blueprint.route('/agregar', methods=['GET', 'POST'])
def agregar_pelicula():
    if request.method == 'POST':
        nombre = request.form['nombre']
        genero = request.form['genero']
        duracion = request.form['duracion']
        inventario = request.form['inventario']

        #Si no funciona, agregar dos e en nombre y dos l en email

        nueva_pelicula = Pelicula(nombre=nombre, genero=genero, duracion=duracion, inventario=inventario)
        try:
            db.session.add(nueva_pelicula)
            db.session.commit()
            flash('Película agregada correctamente', 'success')
            return redirect(url_for('pelicula.agregar_pelicula'))
        except IntegrityError:
            db.session.rollback()  # Revertir los cambios realizados en la transacción
            flash('Error: El correo electrónico ya está registrado', 'error')
            return redirect(url_for('pelicula.agregar_pelicula'))

    return render_template('Pelicula/add_pelicula.html')


@pelicula_blueprint.route('/borrar', methods=['GET', 'POST'])
def borrar_pelicula():
    if request.method == 'GET':
        return render_template('Usuario/borrar.html')
    else:
        idUsuario = request.form['idUsuario']

        usuario_a_eliminar = Usuario.query.get(idUsuario)
        # nuevo_usuario = Usuario(nombre=nombre, password=password, email=email)
        if usuario_a_eliminar:
            db.session.delete(usuario_a_eliminar)
            db.session.commit()
            return 'Usuario eliminado'
            flash('Usuario eliminado correctamente', 'success')
        else:
            return 'Usuario no encontrado'
