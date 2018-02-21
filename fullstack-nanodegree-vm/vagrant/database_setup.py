import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))


class Cuisine(Base):
	__tablename__ = 'cuisine'

	id = Column(Integer, primary_key = True)
	name = Column(String(250), nullable = False)
	user_id = Column(Integer, ForeignKey('user.id'))
	user = relationship(User)

	@property
	def serialize(self):
	# Returns object in easily serializable format
		return {
			'id' : self.id,
			'name' : self.name,
		}

class Recipe(Base):
	__tablename__ = 'recipe'
	id = Column(Integer, primary_key = True)
	name = Column(String(250), nullable = False)
	description = Column(String(250))
	preptime = Column(String(8))
	course = Column(String(250))
	cuisine_id = Column(Integer, ForeignKey('cuisine.id'))
	cuisine = relationship(Cuisine)
	user_id = Column(Integer, ForeignKey('user.id'))
	user = relationship(User)

	@property
	def serialize(self):
		# Return object in easily serializable format
		return {
			'id' : self.id,
			'name' : self.name,
			'description' : self.description,
			'preptime' : self.preptime,
			'course' : self.course,
		}

engine = create_engine('sqlite:///cuisinerecipewithusers.db')
Base.metadata.create_all(engine)