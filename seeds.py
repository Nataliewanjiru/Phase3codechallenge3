from sqlalchemy.orm import sessionmaker
from sqlalchemy import engine, create_engine, insert
from sqlalchemy.ext.declarative import declarative_base
from tables import *

DATABASE_URI = 'sqlite:///database.db'

engine = create_engine(DATABASE_URI, echo=True)

Base = declarative_base()

Session = sessionmaker(bind = engine)
session = Session()

customer1 = Customer(first_name ="Natalie", last_name = "Wanjiru")
customer2= Customer(first_name ="Mary", last_name = "Mwangi")
customer3 = Customer(first_name ="Ivy", last_name = "Wambui")

restaurant1 = Restaurant(restaurant_name = "Pepino",restaurant_price = 1000)
restaurant2 = Restaurant(restaurant_name = "Pizza Inn",restaurant_price = 2000)
restaurant3 = Restaurant(restaurant_name = "Chicken Inn",restaurant_price = 3000)

review1 = Review(star_rating = 3, restaurant_id = 1 , customer_id = 1)

stmt = insert(customerrestaurant).values(
    restaurant_id=restaurant1.id,
    customer_id=customer1.id
)


#session.add(customer3)
#session.add(restaurant1)
#session.add(restaurant2)
#session.add(restaurant3)
#session.add(stmt)

session.execute(stmt)

session.commit()

session.close()