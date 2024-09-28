from flask import Flask, request, jsonify
from flask_migrate import Migrate
from models import db, User, Favorites, Animal_type, Ster_state, Location, Pets
from flask_cors import CORS

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///mibasededatos.db'
db.init_app(app)
migrate = Migrate(app, db)
CORS(app)

@app.route('/', methods = ['GET'])
def home():
    return "Welcome"



if __name__ == "__main__":
  app.run(host='localhost', port=5002, debug=True)