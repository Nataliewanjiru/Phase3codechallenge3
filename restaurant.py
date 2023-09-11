from sqlalchemy import Column, Integer, String,create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


DATABASE_URI = 'sqlite:///database.db'

engine = create_engine(DATABASE_URI)

Base = declarative_base()

class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer, primary_key=True)
    restaurant_name = Column(String(100), nullable=False)
    restaurant_price = Column(Integer)


    #method used to get all the reviews of the restaurant
    def get_reviews(self,table, session, restaurant_id):
     restaurant_reviews = (session.query(table).filter(table.restaurant_id == restaurant_id).all())
     for review in restaurant_reviews:
        print(f"Star Rating for the restaurant: {review.star_rating}")

    #method used to get the customer that reviewed the hotel 
    def get_customers(self,table1,table2, session, restaurant_id):
      restaurant_customers = (session.query(table1).filter(table1.restaurant_id == restaurant_id).all())
      for review in restaurant_customers:
        customerName = (session.query(table2).filter(table2.id == review.customer_id).first())
        print(f"Customer Name: {customerName.first_name} {customerName.last_name}")
        

    
# Create a SQLite database
Base.metadata.create_all(bind=engine)


