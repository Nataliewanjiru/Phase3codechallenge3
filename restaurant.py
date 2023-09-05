from sqlalchemy import Column, Integer, String,create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


DATABASE_URI = 'sqlite:///database.db'

engine = create_engine(DATABASE_URI, echo=True)

Base = declarative_base()

class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer, primary_key=True)
    restaurant_name = Column(String(100), nullable=False)
    restaurant_price = Column(Integer)


    
    def  review(self,table,session,restaurant_id):
      restaurant_reviews = (session.query(table).join(self).filter(Restaurant.id == restaurant_id).all())
      for review in restaurant_reviews:
       print(f"Star Rating for the restaurant: {review.star_rating}")

    
    
# Create a SQLite database
Base.metadata.create_all(bind=engine)


