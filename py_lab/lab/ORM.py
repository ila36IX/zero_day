from sqlalchemy import create_engine, Column, Integer, String, text
from sqlalchemy.orm import declarative_base

str_conn = "mysql://alien:200202@localhost:3306/world"
engine = create_engine(str_conn, echo=True)

reuslt = engine.execute()
# con = engine.connect()
# result = con.execute(text("select * from city limit 10"))
#
# print(len(result.keys()))
con.close()

# Base = declarative_base()

# class User(Base):
#     __tablename__ = "users"
#     
#     id = Column(Integer, primary_key=True)
#     name = Column(String(50))
#     username = Column(String(50))
#     def __repr__(self):
#         return f"[{self.name}] ({self.id}):{self.username}"

#
# Base.metadata.create_all(bind=engine)
