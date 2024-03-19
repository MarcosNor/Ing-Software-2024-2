from flask import Blueprint, request, render_template, flash, redirect, url_for
from sqlalchemy import DateTime, func
from sqlalchemy.exc import IntegrityError

from alchemyClasses.Rentar import Rentar, db
from alchemyClasses.Usuario import Usuario
from alchemyClasses.Pelicula import Pelicula

rentar_blueprint = Blueprint('rentar', __name__, url_prefix='/rentar')

@rentar_blueprint.route('/', methods=['GET'])
def raiz():
    return render_template('Rentar/raiz.html')

@rentar_blueprint.route('/ver_todos', methods=['GET'])
def ver_rentas():
    rentas = db.session.query(Rentar, Usuario, Pelicula).join(Usuario).join(Pelicula).all()
    return render_template('Rentar/ver_todos.html', rentas=rentas)

@rentar_blueprint.route('/agregar', methods=['GET', 'POST'])
def agregar_renta():
    if request.method == 'POST':
        id_usuario = request.form['idUsuario']
        id_pelicula = request.form['idPelicula']
        fecha_renta = func.now()
        dias_de_renta = request.form.get('dias_de_renta', 5)
        estatus = 0

        nueva_renta = Rentar(idUsuario=id_usuario, idPelicula=id_pelicula, fecha_renta=fecha_renta, dias_de_renta=dias_de_renta, estatus=estatus)
        try:
            db.session.add(nueva_renta)
            db.session.commit()
            flash('Renta agregada correctamente', 'success')
            return redirect(url_for('rentar.agregar_renta'))
        except IntegrityError:
            db.session.rollback()  # Revertir los cambios realizados en la transacción
            flash('Error al agregar la renta', 'error')
            return redirect(url_for('rentar.agregar_renta'))

    return render_template('Rentar/add_renta.html')

@rentar_blueprint.route('/actualizar', methods=['GET', 'POST'])
def actualizar_renta():
    if request.method == 'POST':
        id_rentar = int(request.form['idRentar'])
        nuevo_valor = request.form['nuevoValor']

        rentar = Rentar.query.get(id_rentar)
        if rentar:
            if hasattr(rentar, nuevo_valor):
                setattr(rentar, rentar.estatus, nuevo_valor)
                db.session.commit()
                flash('Estatus actualizado correctamente', 'success')
                return render_template('Rentar/actualizar.html')
            else:
                flash('No se puede actualizar el campo', 'error')
        else:
            flash('Renta no encontrada', 'error')
    return render_template('Rentar/actualizar.html')
