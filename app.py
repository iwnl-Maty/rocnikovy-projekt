import app
from flask import Flask, render_template, request, redirect, url_for, flash# type: ignore
from flask_sqlalchemy import SQLAlchemy # type: ignore
from flask_migrate import Migrate # type: ignore
from flask_login import current_user
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://matypiernik:projektos@localhost/mydatabase'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Place(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    image = db.Column(db.String(200), nullable=True)

class PointOfInterest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

@app.route('/add_point', methods=['GET', 'POST'])
def add_point():
    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')
        latitude = request.form.get('latitude')
        longitude = request.form.get('longitude')

        if not name or not latitude or not longitude:
            flash('Prosím, vyplňte všechna povinná pole!', 'error')
            return redirect(url_for('add_point'))

        try:
            new_point = PointOfInterest(
                name=name,
                description=description,
                latitude=float(latitude),
                longitude=float(longitude)
            )
            db.session.add(new_point)
            db.session.commit()
            flash('Bod zájmu byl úspěšně přidán!', 'success')
            return redirect(url_for('home'))
        except Exception as e:
            db.session.rollback()
            flash(f'Nastala chyba při ukládání: {e}', 'error')
            return redirect(url_for('add_point'))

    return render_template('add_point.html')