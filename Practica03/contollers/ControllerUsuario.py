from flask import Blueprint, request, render_template, flash, redirect, url_for
from sqlalchemy.exc import IntegrityError

from alchemyClasses.Rentar import Rentar
from alchemyClasses.Usuario import Usuario, db

usuario_blueprint = Blueprint('usuario', __name__, url_prefix='/usuario')

@usuario_blueprint.route('/', methods=['GET'])
def raiz():
    return render_template('Usuario/raiz.html')

@usuario_blueprint.route('/ver_todos', methods=['GET'])
def ver_usuarios():
    usuarios = Usuario.query.all()
    return render_template('Usuario/ver_todos.html', usuarios=usuarios)

@usuario_blueprint.route('/id/<int:id_usuario>/<string:nombre>')
def ver_usuario_id(id_usuario, nombre):
    usuario = Usuario.query.filter_by(idUsuario=id_usuario).first()
    if usuario:
        return f"Nombre: {usuario.nombre}, Email: {usuario.email}"
    else:
        return "Usuario no encontrado"

@usuario_blueprint.route('/agregar', methods=['GET', 'POST'])
def agregar_usuario():
    if request.method == 'POST':
        nombre = request.form['nombre']
        ap_pat = request.form['apPat']
        ap_mat = request.form['apMat']
        passwd = request.form['password']
        email = request.form['email']
        #profilePictureU = request.form['profilePicture']
        #superUserU = request.form['superUser']

        nuevo_usuario = Usuario(nombre=nombre, apPat=ap_pat, apMat=ap_mat, password=passwd, email=email,
                                profilePicture=None, superUser=0)
        try:
            db.session.add(nuevo_usuario)
            db.session.commit()
            flash('Usuario agregado correctamente', 'success')
            return redirect(url_for('usuario.agregar_usuario'))
        except IntegrityError:
            db.session.rollback()  # Revertir los cambios realizados en la transacción
            flash('Error: El correo electrónico ya está registrado', 'error')
            return redirect(url_for('usuario.agregar_usuario'))

    return render_template('Usuario/add_user.html')


@usuario_blueprint.route('/borrar', methods=['GET', 'POST'])
def borrar_usuario():
    if request.method == 'GET':
        return render_template('Usuario/borrar.html')
    else:
        idUsuario = request.form['idUsuario']
        usuario_a_eliminar = Usuario.query.get(idUsuario)

        if usuario_a_eliminar:
            rentas_asociadas = Rentar.query.filter_by(idUsuario=idUsuario).all()
            for renta in rentas_asociadas:
                db.session.delete(renta)
                db.session.commit()

            db.session.delete(usuario_a_eliminar)
            db.session.commit()
            flash('Usuario eliminado correctamente', 'success')
            return redirect(url_for('usuario.borrar_usuario'))
        else:
            flash('Error: No se encontró el usuario', 'error')
            return redirect(url_for('usuario.borrar_usuario'))


@usuario_blueprint.route('/actualizar', methods=['GET', 'POST'])
def actualizar_usuario():
    if request.method == 'POST':
        id_usuario = int(request.form['idUsuario'])
        actualiza = request.form['campoActualizar']
        nuevo_valor = request.form['nuevoValor']

        usuario = Usuario.query.get(id_usuario)
        if usuario:
            if hasattr(usuario, actualiza):
                setattr(usuario, actualiza, nuevo_valor)
                db.session.commit()
                flash('Usuario actualizado correctamente', 'success')
                return render_template('Usuario/actualizar.html')
            else:
                flash('No se puede actualizar el campo', 'error')
        else:
            flash('Usuario no encontrado', 'error')
    return render_template('Usuario/actualizar.html')