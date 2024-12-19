from flask import Flask, render_template # type: ignore

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('map.html')

if __name__ == "__main__":
    app.run(debug=True)