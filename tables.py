from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table, text
from sqlalchemy.orm import relationship,session
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URI = 'sqlite:///database.db'

engine = create_engine(DATABASE_URI, echo=True)

Base = declarative_base()


sql_statement = text("SELECT * FROM reviews")  # Replace 'your_table_name' with your actual table name

# Execute the SQL statement
with engine.connect() as connection:
    result = connection.execute(sql_statement)
    rows = result.fetchall()






# Define a new table that represents the many-to-many relationship
customerrestaurant = Table(
    'customerrestaurant',
    Base.metadata,
    Column('restaurant_id', Integer, ForeignKey('restaurants.id')),
    Column('customer_id', Integer, ForeignKey('customers.id'))
)




class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer, primary_key=True)
    restaurant_name = Column(String(100), nullable=False)
    restaurant_price = Column(Integer)

    @classmethod
    def  customer(cls,session,restaurant_id):
      restaurant_customers = (
       session.query(Review)
       .join(cls)  
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

        
    @classmethod
    def  review(cls,session,restaurant_id):
      restaurant_reviews = (
         session.query(Review)
         .join(cls)  
         .filter(Restaurant.id == restaurant_id)  
         .all()
        )
 # Print the star ratings of the customer's reviews
      for review in restaurant_reviews:
        print(f"Star Rating for the restaurant: {review.star_rating}")


    # Establish a one-to-many relationship between Restaurant and Review
    reviews = relationship("Review", back_populates="restaurant")

    # Establish a many-to-many relationship with Customer
    customers = relationship("Customer", secondary=customerrestaurant, back_populates="restaurants")

    


class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)

    @classmethod
    def  review(cls,session,customer_id):
        customer_reviews = (
           session.query(Review)
           .join(cls)  
           .filter(Customer.id == customer_id)  
           .all()
           )

        # Print the star ratings of the customer's reviews
        for review in customer_reviews:
             print(f"Star Rating: {review.star_rating}")


    
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





    
    # Establish a one-to-many relationship between Customer and Review
    reviews = relationship("Review", back_populates="customer")

    # Establish a many-to-many relationship with Restaurant
    restaurants = relationship("Restaurant", secondary=customerrestaurant, back_populates="customers")




class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    star_rating = Column(Integer, nullable=False)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'), nullable=False)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)

    # Define relationships
    restaurant = relationship("Restaurant", back_populates="reviews")
    customer = relationship("Customer", back_populates="reviews")

    def customer(self):
        return self.customer
    
    def restaurant(self):
        return self.restaurant

# Create a SQLite database
Base.metadata.create_all(bind=engine)


