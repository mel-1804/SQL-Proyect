from flask import Flask, request, jsonify
from flask_migrate import Migrate
from models import db, User, Favorites, Animal_type, Ster_state, Location, Pets
from flask_cors import CORS

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///mibasededatos.db'
db.init_app(app)
migrate = Migrate(app, db)
CORS(app)


#------------------------------------------INDEX
@app.route('/', methods = ['GET'])
def home():
    return "Welcome"

#------------------------------------------USERS
@app.router('/createUser', methods=['POST'])
def create_user():

  data= request.json
  usuario = User()

  usuario.name = data['name']
  usuario.lastname = data['lastname']
  usuario.email = data['email']
  usuario.password = data['password']

  db.session.add(usuario)
  db.session.commit()

    return{
      "message": "User created successfully",
      "data": usuario.serialize()
    }, 201

#--------------------------------------------PETS
@app.router('/createPet', methods=['POST'])
def create_pet():

  data= request.json
  mascota = Pets()

  mascota.name = data['name']
  mascota.animal_type_id = data['animalTypeId']
  mascota.gender = data['gender']
  mascota.age_months = data['ageMonths']

  db.session.add(mascota)
  db.session.commit()

    return{
      "message": "Pet created successfully",
      "data": mascota.serialize()
    }, 201

#-----------------------------------LOCATIONS
@app.router('/createLocation', methods=['POST'])
def create_location():

  data= request.json
  locacion = Location()

  locacion.region = data['region']
  locacion.comuna = data['comuna']
  
  db.session.add(locacion)
  db.session.commit()

    return{
      "message": "Location created successfully",
      "data": locacion.serialize()
    }, 201


if __name__ == "__main__":
  app.run(host='localhost', port=5002, debug=True)