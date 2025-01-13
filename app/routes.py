from flask import Blueprint, render_template, redirect, url_for, request, flash, jsonify  # type: ignore
from flask_login import login_user, logout_user, login_required, current_user  # type: ignore
from .models import User, PointOfInterest
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    points = PointOfInterest.query.all()
    points_dict = [{"id": p.id, "name": p.name, "description": p.description, "latitude": p.latitude, "longitude": p.longitude} for p in points]
    return render_template('index.html', points=points_dict)

@main.route('/detail/<int:point_id>')
def detail(point_id):
    point = PointOfInterest.query.get_or_404(point_id)
    return render_template('detail.html', point=point)

@main.route('/add', methods=['GET', 'POST'])
@login_required
def add_point():
    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')
        latitude = request.form.get('latitude')
        longitude = request.form.get('longitude')

        new_point = PointOfInterest(
            name=name,
            description=description,
            latitude=float(latitude),
            longitude=float(longitude),
            added_by=current_user.id
        )
        db.session.add(new_point)
        db.session.commit()
        flash('Bod zájmu byl přidán!')
        return redirect(url_for('main.index'))

    return render_template('add_point.html')