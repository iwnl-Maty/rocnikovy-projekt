from flask import Flask, render_template, request # type: ignore
from flask_sqlalchemy import SQLAlchemy # type: ignore
from flask_migrate import Migrate # type: ignore

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Place(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    image = db.Column(db.String(200), nullable=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/detail')
def detail():
    name = request.args.get('name', 'Neznámé místo')
    description = request.args.get('description', 'Bez popisu')
    image = request.args.get('image', '')
    return render_template('detail.html', name=name, description=description, image=image)

if __name__ == "__main__":
    app.run(debug=True)