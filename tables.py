from sqlalchemy import create_engine
from sqlalchemy.orm import relationship,session
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URI = 'sqlite:///database.db'

engine = create_engine(DATABASE_URI, echo=True)

Base = declarative_base()



## Execute the SQL statement
#with engine.connect() as connection:
#    result = connection.execute(sql_statement)
#    rows = result.fetchall()#




    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#
  #      
  #  @classmethod
  #  def  review(cls,session,restaurant_id):
  #    restaurant_reviews = (
  #       session.query(Review)
  #       .join(cls)  
  #       .filter(Restaurant.id == restaurant_id)  
  #       .all()
  #      )
 ## Print the star ratings of the customer's reviews
  #    for review in restaurant_reviews:
  #      print(f"Star Rating for the restaurant: {review.star_rating}")
#
#
  #  
  #  
#
#
#
#
  # 
  #  
#
  #  @classmethod
  #  def  review(cls,session,customer_id):
  #      customer_reviews = (
  #         session.query(Review)
  #         .join(cls)  
  #         .filter(Customer.id == customer_id)  
  #         .all()
  #         )
#
  #      # Print the star ratings of the customer's reviews
  #      for review in customer_reviews:
  #           print(f"Star Rating: {review.star_rating}")
#
#
  #  
  #  @classmethod
  #  def  restaurant(cls,session,customer_id):
  #    customer_restaurant = (
  #     session.query(Review)
  #     .join(cls)  
  #     .filter(Customer.id == customer_id)  
  #     .all()
  #     )
  #    
  #    for restaurant in customer_restaurant:
  #          restaurant_name = (
  #           session.query(Restaurant)
  #           .join(Review)  
  #           .filter(Review.id == restaurant.customer_id)  
  #           .all()
  #            )
  #          for name in restaurant_name:
  #              print(f"Restaurant Names: {name.restaurant_name}")
#
  #   
  #  @classmethod
  #  def  full_name(cls,session,customer_id):
  #    customer_name = (
  #     session.query(Review)
  #     .join(cls)  
  #     .filter(Customer.id == customer_id)  
  #     .all()
  #     )
  #
  #    for customer in customer_name:
  #      name = (
  #       session.query(Customer)
  #       .join(Review)  
  #       .filter(Review.id == customer.customer_id)  
  #       .all()
  #        )
  #      for name in name:
  #          print(f"customer Names: {name.first_name} + {name.last_name}")
 #
#
#
  #  
  #  
  #  
#
#
#
#
#
  #  def get_customer(self, session, review_id):
  #   customers = (
  #      session.query(Customer)
  #      .join(Review)  # Join the Customer and Review tables based on the relationship
  #      .filter(Review.id == review_id)
  #      .all()
  #    )
#
  #  # Close the session if needed
  #   return customers
  #     
#

# Create a SQLite database
Base.metadata.create_all(bind=engine)


