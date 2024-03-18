from flask import Blueprint, request, render_template, flash, redirect, url_for
from sqlalchemy.exc import IntegrityError

from alchemyClasses.Usuario import Usuario, db
from model.Model_usuario import borra_usuario

usuario_blueprint = Blueprint('usuario', __name__, url_prefix='/usuario')

@usuario_blueprint.route('/', methods=['GET'])
def raiz():
    return render_template('Usuario/raiz.html')

@usuario_blueprint.route('/ver_todos', methods=['GET'])
def ver_usuarios():
    usuarios = Usuario.query.all()
    for usuario in usuarios:
        print(f"ID: {usuario.idUsuario}, Nombre: {usuario.nombre}, Email: {usuario.email}")
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
        nombree = request.form['nombre']
        ap_pat = request.form['apPat']
        ap_mat = request.form['apMat']
        passwd = request.form['password']
        emaill = request.form['email']
        #profilePictureU = request.form['profilePicture']
        #superUserU = request.form['superUser']

        nuevo_usuario = Usuario(nombre=nombree, apPat=ap_pat, apMat=ap_mat, password=passwd, email=emaill,
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


@usuario_blueprint.route('/borrar',  methods=['GET', 'POST'])
def borrar_usuario():
    #borra_usuario(1)
    return "ola"
