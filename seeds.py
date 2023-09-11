from sqlalchemy.orm import sessionmaker, relationship,declarative_base
from sqlalchemy import create_engine
from customer import *
from restaurant import *
from review import *


# Establish a one-to-many relationship between Customer and Review
reviews = relationship("Review", back_populates="customer")

DATABASE_URI = 'sqlite:///database.db'

engine = create_engine(DATABASE_URI)

Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()

customer1 = Customer(first_name="Natalie", last_name="Wanjiru")
customer2 = Customer(first_name="Mary", last_name="Mwangi")
customer3 = Customer(first_name="Ivy", last_name="Wambui")

restaurant1 = Restaurant(restaurant_name="Pepino", restaurant_price=1000)
restaurant2 = Restaurant(restaurant_name="Pizza Inn", restaurant_price=2000)
restaurant3 = Restaurant(restaurant_name="Chicken Inn", restaurant_price=3000)

review1 = Review(star_rating=3, restaurant_id=1, customer_id=1)
review2 = Review(star_rating=2, restaurant_id=2, customer_id=2)
review3 = Review(star_rating=4, restaurant_id=3, customer_id=3)
review4 = Review(star_rating=4, restaurant_id=3, customer_id=1)
review5 = Review(star_rating=3, restaurant_id=1, customer_id=2)


#session.add(review5)
# Add objects to the session
#session.add_all([customer1, customer2, customer3, restaurant1, restaurant2, restaurant3, review1, review2, review3, review4])

check= restaurant1.get_customers(Review,session,1)
print(check)

# Commit changes to the database
session.commit()

# Close the session
session.close()