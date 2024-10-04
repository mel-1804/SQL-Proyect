from flask import Flask, request, jsonify
from flask_migrate import Migrate
from models import db, User, Favorites, Animal_type, Ster_state, Location, Pets
from flask_cors import CORS

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///mibasededatos.db'
db.init_app(app)
migrate = Migrate(app, db)
CORS(app)


#------------------------------------------HOME
@app.route('/', methods = ['GET'])
def home():
    return "Welcome"


#------------------------------------------USERS
@app.route('/createUser', methods=['POST'])
def create_user():

  data= request.json
  user = User()

  user.name = data['name']
  user.lastname = data['lastname']
  user.email = data['email']
  user.password = data['password']

  db.session.add(user)
  db.session.commit()

  return{
    "message": "User created successfully",
    "data": user.serialize()
  }, 201


#--------------------------------------------PETS
@app.route('/createPet', methods=['POST'])
def create_pet():

  data= request.json
  pet = Pets()

  pet.name = data['name']
  pet.animal_type_id = data['animalTypeId']
  pet.gender = data['gender']
  pet.age_months = data['ageMonths']

  db.session.add(pet)
  db.session.commit()

  return{
    "message": "Pet created successfully",
    "data": pet.serialize()
  }, 201


#-----------------------------------LOCATIONS
@app.route('/createLocation', methods=['POST'])
def create_location():

  data= request.json
  location = Location()

  location.region = data['region']
  location.comuna = data['comuna']
  
  db.session.add(location)
  db.session.commit()

  return{
    "message": "Location created successfully",
    "data": location.serialize()
  }, 201


#-----------------------------------ANIMAL TYPE
@app.route('/createSterState', methods=['POST'])
def create_sterilization_state():

  data= request.json
  ster_state = Ster_state()

  ster_state.status = data['status']
    
  db.session.add(ster_state)
  db.session.commit()

  return{
    "message": "sterilization state created successfully",
    "data": ster_state.serialize()
  }, 201


#-----------------------------------ANIMAL TYPE
@app.route('/createAnimalType', methods=['POST'])
def create_animal_type():

  data= request.json
  animal_type = Animal_type()

  animal_type.animal = data['animal']
    
  db.session.add(animal_type)
  db.session.commit()

  return{
    "message": "animal type created successfully",
    "data": animal_type.serialize()
  }, 201


if __name__ == "__main__":
  app.run(host='localhost', port=5002, debug=True)