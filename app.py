from flask import Flask, render_template, request # type: ignore

app = Flask(__name__)

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