from this import d
from fastapi import FastAPI, Depends
from pydantic import BaseModel
from typing import Optional, List
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from sqlalchemy import Boolean, Column, Float, String, Integer


app = FastAPI()


# SqlAlchemy Setup

# defining the sql alchemy engine here.
SQLALCHEMY_DATABASE_URL = 'sqlite+pysqlite:///./db.sqlite3:'
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True, future=True)

# blueprint for a SQLALCHEMY Session
SessionLocal = sessionmaker(autocommit=False, autoflush=False,bind=engine)

# defines a base model, that is used to define Python objects as SQLAlchemy ORM objects
Base = declarative_base()

# Dependency, this is really interesting...
def get_db():
    """instantiates a session and closes it when done."""

    db = SessionLocal()
    try:
        yield db
    finally: 
        db.close()

# define an Place SQLAlchemy model
class DBPlace(Base):
    __tablename__ = 'places'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    description = Column(String, nullable=True)
    coffee = Column(Boolean)
    wifi = Column(Boolean)
    food = Column(Boolean)
    lat = Column(Float)
    lng = Column(Float)

Base.metadata.create_all(bind=engine)


# defining a pydantic model to represent a Place.
# it relies heavily on the python3 typing. 
class Place(BaseModel):
    name: str
    description: Optional[str] = None
    coffee: bool
    wifi: bool
    food: bool
    lat: float
    lng: float


    class Config:
        """Allows us to hook up a database"""
        orm_mode = True


# methods for interacting with the database...

def get_place(db: Session, place_id:int):
    """returns a single place object"""
    return db.query(DBPlace).where(DBPlace.id == place_id).first()

def get_places(db: Session):
    """returns all the place objects"""
    return db.query(DBPlace).all()


def create_place(db:Session, place: Place):
    """inserts a new place object into the database"""
    db_place = DBPlace(**place.dict())
    db.add(db_place)
    db.commit()
    db.refresh(db_place)

    return db_place


@app.post('/places/',  response_model=Place)
def create_places_view(place: Place, db: Session = Depends(get_db)):
    """route for creating a a new place"""
    db_place = create_place(db, place)
    return db_place

@app.get('/places/', response_model=List[Place])
def get_places_view(db:Session = Depends(get_db)):
    """route for returning all place objects from the db"""
    return get_places(db)

# both of the above routes are defined from the same endpoint, the http method 
# which functions are called. 
# when a get request is sent the get_place_view is called 
# and when a post request is sent the create_places_view is called.

@app.get('/place/{place_id}')
def get_place_view(place_id: int, db:Session=Depends(get_db)):
    """route for returning a single place object"""
    return get_place(db, place_id)

@app.get('/')
async def root():
    return {'message': 'Welcome here!!'}
