from sqlalchemy import  Column, Integer, String,create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from restaurant import Restaurant


DATABASE_URI = 'sqlite:///database.db'

engine = create_engine(DATABASE_URI)

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)


   #method that gives all the customer rating the table refers to the review table
    @classmethod
    def review(cls,table,session,customer_id):
        customer_reviews = (session.query(table).join(cls).filter(Customer.id == customer_id).all())
    # Print the star ratings of the customer's reviews
        for review in customer_reviews:
             print(f"Star Rating: {review.star_rating}")



    #method that gives the restaurant rated the table refers to the review table
    @classmethod
    def  restaurant(cls,table,session,customer_id):
      customer_restaurant = (session.query(table).join(cls).filter(Customer.id == customer_id).all())
  
      for restaurant in customer_restaurant:
         restaurant_name = (session.query(Restaurant).join(table).filter(table.id == restaurant.customer_id).all())
         for name in restaurant_name:
            print(f"Restaurant Names: {name.restaurant_name}")
 

 
     #method that gives restaurant full name the table refers to review table
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    @classmethod
    def favourite_restaurant(cls, table, session, customer_id):
      # Query customer reviews, join with the provided table (assuming it's a review table)
      customer_reviews = (session.query(table).join(Customer).filter(Customer.id == customer_id).order_by(table.star_rating.desc()).all())
   
      if customer_reviews:
          # Get the highest-rated review (first in the sorted list)
          highest_rated_review = customer_reviews[0]
   
          # Retrieve the associated restaurant
          restaurant = (session.query(Restaurant).join(table).filter(table.id == highest_rated_review.id).first())
   
          if restaurant:
              print(f"Favorite Restaurant: {restaurant.restaurant_name} with {highest_rated_review.star_rating} stars")
          else:
              print("The highest-rated review is associated with an unknown restaurant.")
      else:
          print("This customer hasn't reviewed any restaurants yet.")

   
    def add_review(self, table, restaurant, rating,customerId, session):
        # Create a new Review instance with the provided rating and customer_id
        new_review = table(star_rating=rating,restaurant_id=restaurant, customer_id=customerId )

        # Add the new review to the session and commit it to the database
        session.add(new_review)
        session.commit()




      
    
   





# Create a SQLite database
Base.metadata.create_all(bind=engine)
