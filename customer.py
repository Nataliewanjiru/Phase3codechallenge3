from sqlalchemy import  Column, Integer, String,create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


DATABASE_URI = 'sqlite:///database.db'

engine = create_engine(DATABASE_URI, echo=True)

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)

# Establish a one-to-many relationship between Customer and Review
reviews = relationship("Review", back_populates="customer")

# Create a SQLite database
Base.metadata.create_all(bind=engine)
