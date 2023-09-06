from sqlalchemy import  Column, Integer, String,create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from restaurant import Restaurant


DATABASE_URI = 'sqlite:///database.db'

engine = create_engine(DATABASE_URI, echo=True)

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)

   
   

   #method that gives all the customer rating
    @classmethod
    def review(cls,table,session,customer_id):
        customer_reviews = (session.query(table).join(cls).filter(Customer.id == customer_id).all())
    # Print the star ratings of the customer's reviews
        for review in customer_reviews:
             print(f"Star Rating: {review.star_rating}")

    #method that gives the restaurant rated
    @classmethod
    def  restaurant(cls,table,session,customer_id):
      customer_restaurant = (session.query(table).join(cls).filter(Customer.id == customer_id).all())
  
      for restaurant in customer_restaurant:
         restaurant_name = (session.query(Restaurant).join(table).filter(table.id == restaurant.customer_id).all())
         for name in restaurant_name:
            print(f"Restaurant Names: {name.restaurant_name}")
 
     #method that gives restaurant full name
    def full_name(self):
        print(f"{self.first_name} {self.last_name}")
        return f"{self.first_name} {self.last_name}"
    
    
    






# Create a SQLite database
Base.metadata.create_all(bind=engine)
