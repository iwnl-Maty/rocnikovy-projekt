from flask import Blueprint, render_template, redirect, url_for, request, flash  # type: ignore
from flask_login import login_user, logout_user, login_required, current_user  # type: ignore
from .models import User, PointOfInterest
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    points = PointOfInterest.query.all()  # Načtení všech bodů zájmu z databáze
    points_dict = [point.to_dict() for point in points]  # Serializace bodů do JSON formátu
    return render_template('index.html', points=points_dict)

@main.route('/detail/<int:point_id>')
def detail(point_id):
    point = PointOfInterest.query.get_or_404(point_id)  # Načtení bodu zájmu podle ID
    return render_template('detail.html', point=point)

@main.route('/add', methods=['GET', 'POST'])
@login_required
def add_point():
    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')
        latitude = request.form.get('latitude')
        longitude = request.form.get('longitude')

        try:
            new_point = PointOfInterest(
                name=name,
                description=description,
                latitude=float(latitude),
                longitude=float(longitude),
                added_by=current_user.id  # Získání ID aktuálního uživatele
            )
            db.session.add(new_point)
            db.session.commit()
            flash('Bod zájmu byl přidán!')
            return redirect(url_for('main.index'))
        except Exception as e:
            db.session.rollback()
            flash(f'Chyba při přidávání bodu: {str(e)}')

    return render_template('add_point.html')

@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()
        if user and user.password == password:  # Jednoduchá kontrola hesla (doporučujeme hashování)
            login_user(user)
            flash('Přihlášení proběhlo úspěšně.')
            return redirect(url_for('main.index'))
        else:
            flash('Špatné přihlašovací údaje.')

    return render_template('login.html')

@main.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Odhlášení proběhlo úspěšně.')
    return redirect(url_for('main.index'))

@main.app_errorhandler(404)
def page_not_found(error):
    """Ošetření chyby 404 pro případ, že URL neexistuje."""
    return render_template('404.html'), 404