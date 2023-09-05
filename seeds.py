from sqlalchemy.orm import sessionmaker
from sqlalchemy import engine, create_engine
from sqlalchemy.orm import declarative_base
from customer import *
from restaurant import Restaurant
from review import *

DATABASE_URI = 'sqlite:///database.db'

engine = create_engine(DATABASE_URI, echo=True)

Base = declarative_base()

# functions for the restaurant
#returns all customers that reviewed
def  customer(session,restaurant_id):
  restaurant_customers = (
   session.query(Review)
   .join(Restaurant)  
   .filter(Restaurant.id == restaurant_id)  
   .all()
   )
  
  for customer in restaurant_customers:
        customer_name = (
         session.query(Customer)
         .join(Review)  
         .filter(Review.id == customer.customer_id)  
         .all()
          )
        for name in customer_name:
            print(f"Customer Names: {name.first_name}")
















  #  

@classmethod
def  restaurant(cls,session,customer_id):
  customer_restaurant = (
   session.query(Review)
   .join(cls)  
   .filter(Customer.id == customer_id)  
   .all()
   )
  
  for restaurant in customer_restaurant:
        restaurant_name = (
         session.query(Restaurant)
         .join(Review)  
         .filter(Review.id == restaurant.customer_id)  
         .all()
          )
        for name in restaurant_name:
            print(f"Restaurant Names: {name.restaurant_name}")
 
@classmethod
def  full_name(cls,session,customer_id):
  customer_name = (
   session.query(Review)
   .join(cls)  
   .filter(Customer.id == customer_id)  
   .all()
   )
  for customer in customer_name:
    name = (
     session.query(Customer)
     .join(Review)  
     .filter(Review.id == customer.customer_id)  
     .all()
      )
    for name in name:
        print(f"customer Names: {name.first_name} + {name.last_name}")
  #  


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



#session.add(customer1)
#session.add(customer2)
#session.add(customer3)
#session.add(restaurant1)
#session.add(restaurant2)
#session.add(restaurant3)
#session.add(review1)
#session.add(review2)
#session.add(review3)
#session.add(review4)

#restaurant1.customer(session,1)
#restaurant2.review(session,2)
customer1.full_name()


session.commit()

#check = review1.full_review(session, 1)
#print(check)

session.close()

