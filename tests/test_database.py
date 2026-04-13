from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from app.database import Base


TEST_BD_URl="sqlite:///./test.db"

engine=create_engine(TEST_BD_URl)
TestingSessionLocal=sessionmaker(bind=engine)

def setup_module():
    Base.metadata.create_all(bind=engine)

def teardown_module():
    Base.metadata.drop_all(bind=engine)
