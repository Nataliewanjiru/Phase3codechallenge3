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


