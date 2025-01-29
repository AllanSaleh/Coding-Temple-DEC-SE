'''
python -m venv venv | python3 -m venv venv
venv\scripts\activate | source venv/bin/activate
pip or pip3 install flask flask-sqlalchemy flask-marshmallow mysql-connector-python marshmallow-sqlalchemy python-dotenv
pip freeze > requirements.txt
'''

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy import ForeignKey, Table, String, Column, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields, Schema, ValidationError
from typing import List, Optional
from dotenv import load_dotenv
import os

app = Flask(__name__)
load_dotenv()
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_NOTIFICATION'] = os.getenv('SQLALCHEMY_TRACK_NOTIFICATION')

class Base(DeclarativeBase):
    pass

db=SQLAlchemy(model_class=Base)
db.init_app(app)
ma = Marshmallow(app)

'''
TODO: Develop CRUD Operations for Trainer
    - POST
    - GET
    - UPDATE
    - DELETE
TODO: Develop CRUD Operations for Pokemon
    - POST
    - GET
    - UPDATE
    - DELETE

'''

trainer_pokemon = Table(
    "trainer_pokemoon",
    Base.metadata,
    Column("trainer_id", ForeignKey("trainers.trainer_id")),
    Column("pokemon_id", ForeignKey("pokemon.pokemon_id"))
)

class Trainer(Base):
    __tablename__ = "trainers"

    trainer_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    email: Mapped[Optional[str]] = mapped_column(String(200))

    pokemon: Mapped[List["Pokemon"]] = relationship(secondary=trainer_pokemon, back_populates='trainers')

class Pokemon(Base):
    __tablename__ = 'pokemon'

    pokemon_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(200))
    type: Mapped[str] = mapped_column(String(200))

    trainers: Mapped[List["Trainer"]] = relationship(secondary=trainer_pokemon, back_populates="pokemon")

class PokemonSchema(SQLAlchemyAutoSchema):
    class Meta: 
        model = Pokemon
        # include_fk = True
        # include_relationships = True
        # load_instance = True

    # pokemon_id = fields.Int()
    # name = fields.Str()
    # type = fields.Str()

    # class Meta:
    #     fields = ('pokemon_id', 'name', 'type')

class TrainerSchema(SQLAlchemyAutoSchema):
    class Meta: 
        model = Trainer
        # load_instance = True
        # include_fk = True
        # include_relationships = True

# ------------------- 

# Serialization => Convert data to JSON | .dumps()
# Deserialization =>  Take JSON convert it to dictionary | .load() method

# include_fk = True or False
# When your model has relationships to other tables and you want the foreign key fields to be explicitly included in the serialized schema.
# So if the FK might show up in your results when you send the data back to the requester

# include_relationships = True or False
# When you have relationships between models and want to include the related data in your schema.
# So if we want to see specific data from a nested schema

# load_instance = True or False
# Use this if you need to deserialize data into actual SQLAlchemy model instances instead of dictionaries.
# If we want to deserialize directly from a request into an object instead of a dictionary

# ------------------- 

trainer_schema = TrainerSchema()
trainers_schema = TrainerSchema(many=True)
pokemon_schema = PokemonSchema()
pokemons_schema = PokemonSchema(many=True)

@app.route('/')
def home():
    return "Hello World"

# POST => Creating data on our database
# GET => Sending data from database to user
# PUT => Updating data on our database
# DELETE => Deleting data on our database. 

@app.route('/trainer', methods=['POST'])
def create_trainer():
    try:
        new_trainer = trainer_schema.load(request.json)
        # new_trainer = TrainerSchema().load(request.json, session=db.session)
    except ValidationError as e:
        return jsonify(e.messages), 400
    print(new_trainer)
    print(type(new_trainer))
    trainer = Trainer(name=new_trainer['name'], email=new_trainer.get('email', ""))
    db.session.add(trainer)
    db.session.commit()

    return trainer_schema.dumps(trainer), 201

@app.route("/trainers", methods=['GET'])
def get_trainer():
    query = select(Trainer)
    trainers = db.session.execute(query).scalars().all()

    print(trainers)

    return trainers_schema.dump(trainers), 200

@app.route("/trainer/<int:id>", methods=['PUT'])
def update_trainer(id):
    name = request.args.get('name')
    email = request.args.get('email')
    # headers
    # args/parameters
    try:
        # new_trainer = trainer_schema.load(request.json)
        name = request.args.get('name')
        email = request.args.get('email')
        print(name, email)
    except ValidationError as e:
        return jsonify(e.messages), 400
    
    query = select(Trainer).where(Trainer.trainer_id == id)
    update_trainer = db.session.execute(query).scalars().first()

    if not update_trainer:
        return jsonify({"Error", "Your id is not valid"})
    
    # for field, attribute in new_trainer.items():
    #     setattr(update_trainer, field, attribute)
    update_trainer.email = email
    update_trainer.name = name
    db.session.commit()

    return jsonify({"Message": "Your pokemon has been updated!"}), 200

@app.route("/trainer/<int:id>", methods=['DELETE'])
def delete_trainer(id):
    delete_trainer = db.session.get(Trainer, id)

    if delete_trainer == None:
        return jsonify({"Error": "There is no id for that trainer on our database"})
    
    db.session.delete(delete_trainer)
    db.session.commit()

    return jsonify({"Message": "Your Trainer has been deleted successfully!"}), 200

# ------------- POKEMON -----------------

@app.route('/pokemon', methods=['POST'])
def create_pokemon():
    try:
        pokemon_data = pokemon_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400
    print(type(pokemon_data))
    new_pokemon = Pokemon(name=pokemon_data['name'], type=pokemon_data['type'])
    db.session.add(new_pokemon)
    db.session.commit()

    return pokemon_schema.dumps(new_pokemon), 201

@app.route('/pokemons', methods=['GET'])
def get_pokemons():
    query = select(Pokemon)
    pokemons = db.session.execute(query).scalars().all()

    return pokemons_schema.dumps(pokemons), 200

@app.route('/pokemon/<int:id>', methods=['PUT'])
def update_pokemon(id):
    try:
        pokemon_data = pokemon_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400
    
    query = select(Pokemon).where(Pokemon.pokemon_id == id)
    pokemon = db.session.execute(query).scalars().first()
    # trainer = db.session.get(Trainer, id) # Can replace query & Trainer

    if pokemon == None:
        return jsonify({"Error": "Pokemon not found"})
    
    for field, value in pokemon_data.items():
        setattr(pokemon, field, value)
    db.session.commit()
    return pokemon_schema.dumps(pokemon), 200

@app.route('/pokemon/<int:id>', methods=['DELETE'])
def delete_pokemon(id):
    delete_pokemon = db.session.get(Pokemon, id)

    if not delete_pokemon:
        return jsonify({"message": "Invalid user id"}), 400
    
    db.session.delete(delete_pokemon)
    db.session.commit()
    return jsonify({"Message": "Trainer was deleted successfully"}), 200

if __name__ == "__main__":
    with app.app_context():
        # db.drop_all()
        db.create_all()
    
    app.run(debug=True)