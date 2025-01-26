import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

    def to_dict(self):
        return {}

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    description = Column(String(250))
    birth_year =Column(String(250))
    gender = Column(String(250))
    height = Column(String(250))
    skin_color = Column(String(250))
    eye_color = Column(String(250))
    hair_color = Column(String(250))
    picture_url = Column(String(250))

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    description = Column(String(250))
    climate = Column(String(250))
    population = Column(String(250))
    orbital_period = Column(String(250))
    rotation_period = Column(String(250))
    diameter = Column(String(250))
    terrain = Column(String(250))

class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    planet_id = Column(Integer, ForeignKey('planet.id'))
    planet = relationship(Planet)
    character_id = Column(Integer, ForeignKey('character.id'))
    character = relationship(Character)


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
