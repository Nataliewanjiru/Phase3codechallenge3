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
    
     # function that return the customer instances
    def get_customer(self,session, review_id):
     customers = (session.query(Customer).join(Review).filter(Review.id == review_id).all())
     return customers 
    #function that returns the restaurant instances
    def get_restaurant(self,session,review_id):
     restaurants = (session.query(Restaurant).join(Review).filter(Review.id == review_id).all())
     return restaurants
    
    #function that returns the reviewed by and what review they have made
    def full_review(self,session,review_id):
     fullName = (session.query(Customer.first_name, Customer.last_name, Review.star_rating).join(Review).filter(Review.id == review_id).all() )
     for name in fullName:
      print(f"Review by {name.first_name}  {name.last_name}: {name.star_rating}")


# Create a SQLite database
Base.metadata.create_all(bind=engine)
