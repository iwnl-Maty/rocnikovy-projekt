import app
from flask import render_template, redirect, url_for, flash, request # type: ignore
from flask_login import login_user, login_required, logout_user, current_user # type: ignore
from werkzeug.security import generate_password_hash, check_password_hash # type: ignore
from . import db
from .models import User, PointOfInterest

@app.route('/')
def index():
    points = PointOfInterest.query.all()
    return render_template('index.html', points=points)

@app.route('/detail/<int:point_id>')
def detail(point_id):
    point = PointOfInterest.query.get_or_404(point_id)
    return render_template('detail.html', point=point)

@app.route('/add', methods=['GET', 'POST'])
@login_required
def add_point():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        latitude = request.form['latitude']
        longitude = request.form['longitude']
        new_point = PointOfInterest(
            name=name,
            description=description,
            latitude=latitude,
            longitude=longitude,
            added_by=current_user.id
        )
        db.session.add(new_point)
        db.session.commit()
        flash('Bod zájmu byl úspěšně přidán!', 'success')
        return redirect(url_for('index'))
    return render_template('add_point.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('index'))
        flash('Nesprávné přihlašovací údaje', 'danger')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))