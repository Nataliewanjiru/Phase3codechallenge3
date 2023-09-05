from sqlalchemy import Column, Integer, String,create_engine
from sqlalchemy.ext.declarative import declarative_base


DATABASE_URI = 'sqlite:///database.db'

engine = create_engine(DATABASE_URI, echo=True)

Base = declarative_base()

class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer, primary_key=True)
    restaurant_name = Column(String(100), nullable=False)
    restaurant_price = Column(Integer)



# Create a SQLite database
Base.metadata.create_all(bind=engine)


