from flask import Flask, jsonify, render_template

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/data')
def get_data():
    return jsonify({"message": "Hello, Flask!", "status": "success"})

if __name__ == '__main__':
    app.run(debug=True)
