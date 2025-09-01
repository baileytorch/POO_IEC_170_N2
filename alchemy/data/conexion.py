from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql+mysqlconnector://root:@localhost:3306/iec_170_n2"
motor_db = create_engine(DATABASE_URL)
Session = sessionmaker(bind=motor_db)
