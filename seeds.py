from sqlalchemy.orm import sessionmaker
from sqlalchemy import engine, create_engine
from sqlalchemy.ext.declarative import declarative_base
from customer import Customer
from restaurant import Restaurant
from review import Review

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
review2 =Review(star_rating=2, restaurant_id=2, customer_id=2)
review3 = Review(star_rating=4, restaurant_id = 3, customer_id = 3)
review4 = Review(star_rating=4, restaurant_id = 3, customer_id = 1)



session.add(customer1)
session.add(customer2)
session.add(customer3)
session.add(restaurant1)
session.add(restaurant2)
session.add(restaurant3)
session.add(review1)
session.add(review2)
session.add(review3)
session.add(review4)

#restaurant1.customer(session,1)
#restaurant2.review(session,2)
#customer1.restaurant(session,1)
#

session.commit()

#check = review1.get_customer(session, 1)
#print(check)
#
session.close()

