from sqlalchemy import create_engine, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from customer import Customer
from restaurant import Restaurant


DATABASE_URI = 'sqlite:///database.db'

engine = create_engine(DATABASE_URI, echo=True)

Base = declarative_base()

class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    star_rating = Column(Integer, nullable=False)
    restaurant_id = Column(Integer, ForeignKey(Restaurant.id))
    customer_id = Column(Integer, ForeignKey(Customer.id))
    


# Create a SQLite database
Base.metadata.create_all(bind=engine)
