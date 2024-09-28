from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Pets(db.Model):
    __tablename__ = "pets"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    # animal_type_id = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(50), nullable=False)
    age_months = db.Column(db.Integer, nullable=False)
    animal_type = db.Relationship("Animal_type", uselist=False)
    sterilization = db.Relationship("Ster_state", uselist=False)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'animalTypeId': self.animal_type_id,
            'gender': self.gender,
            'ageMonths': self.age_months
        }

class Location(db.Model):
    __tablename__ = "location"
    id = db.Column(db.Integer, primary_key=True)
    region = db.Column(db.String(50), nullable=False)
    comuna = db.Column(db.String(50), nullable=False)
    pet_id = db.Column(db.Integer, db.ForeignKey('pets.id'))

    def serialize(self):
        return {
            'id': self.id,
            'region': self.region,
            'comuna': self.comuna,
            'petId': self.pet_id
        }

class Ster_state(db.Model):
    __tablename__ = "sterilization_state"
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(50), nullable=False)
    pet_id = db.Column(db.Integer, db.ForeignKey('pets.id'))

    def serialize(self):
        return {
            'id': self.id,
            'petId': self.pet_id,
            'status': self.status, 
        }


class Animal_type(db.Model): 
    __tablename__ = "animal_type"
    animal = db.Column(db.String(50), nullable=False)
    id = db.Column(db.Integer, db.ForeignKey('pets.id'))

    def serialize(self):
        return {
            'id': self.id,
            'animal': self.animal
        }

  
class Favorites(db.Model):
    __tablename__ = "favorites"
    id = db.Column(db.Integer, primary_key=True)
    pets_id = db.Column(db.Integer, nullable=False, unique=True)
    pets_id = db.Column(db.Integer, db.ForeignKey('pets.id'))
    loc_id = db.Column(db.Integer, nullable=False, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def serialize(self):
        return {
            'id': self.id,
            'petsId': self.pets_id,
            'locID': self.loc_id,
            'userID': self.user_id  
        }
    

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    # favorites = db.Relationship("Favorites", backref="author", lazy=True)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'lastname': self.lastname,
            'email': self.email,
            'password': self.password
        }
    
  

  


 
 