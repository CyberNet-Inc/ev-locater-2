from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import requests

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.db'
db = SQLAlchemy(app)

# Database Model
class ToDo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(200), nullable=False)

db.create_all()

@app.route('/')
def home():
    todos = ToDo.query.all()
    return render_template('index.html', todos=todos)

@app.route('/add_todo', methods=['POST'])
def add_todo():
    task_content = request.form['content']
    new_task = ToDo(task=task_content)
    db.session.add(new_task)
    db.session.commit()
    return jsonify(success=True)

@app.route('/api/ev-chargers', methods=['GET'])
def get_ev_chargers():
    # Mock response (you would replace this with actual API calls)
    response = {
        'chargers': [
            {'name': 'Charger 1', 'lat': -25.7461, 'lng': 28.1881},
            {'name': 'Charger 2', 'lat': -23.8859, 'lng': 30.4742},
        ]
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
