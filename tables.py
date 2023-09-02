from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URI = 'sqlite:///database.db'

engine = create_engine(DATABASE_URI, echo=True)

Base = declarative_base()


sql_statement = text("SELECT * FROM Review")  # Replace 'your_table_name' with your actual table name

# Execute the SQL statement
with engine.connect() as connection:
    result = connection.execute(sql_statement)
    rows = result.fetchall()

# Display the retrieved data on the console
for row in rows:
    print(row)


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

    # Establish a one-to-many relationship between Restaurant and Review
    reviews = relationship("Review", back_populates="restaurant")

    # Establish a many-to-many relationship with Customer
    customers = relationship("Customer", secondary=customerrestaurant, back_populates="restaurants")

    


class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
     
    
    
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

# Create a SQLite database
Base.metadata.create_all(bind=engine)


