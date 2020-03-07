from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/')
def wishes():
	return render_template('wishes.html')

if __name__ == "__main__":
    app.run() # add debug mode
