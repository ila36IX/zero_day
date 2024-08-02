#!/usr/bin/python3
from sqlalchemy import create_engine, func,text, Column, String, DateTime, Integer, Numeric, ForeignKey, Table
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from faker import Faker
# To clean database if needed
from sqlalchemy import MetaData


db_str = "mysql://alien:200202@localhost:3360/testing"
engine = create_engine(db_str)

Base = declarative_base() 
fake = Faker()


middle_table = Table('student_course',
                     Base.metadata,
                     Column('student_id', Integer, ForeignKey('students.id')),
                     Column('course_id', Integer, ForeignKey('courses.id'))
                )

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50), default=fake.first_name(), nullable=False)
    last_name = Column(String(50), default=fake.last_name(), nullable=False)
    courses = relationship('Course', secondary=middle_table, back_populates="students")

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(1024), default=fake.sentence(), nullable=False)
    students = relationship('Student', secondary=middle_table, back_populates="courses")

session = sessionmaker(bind=engine)()

Base.metadata.create_all(bind=engine)

def clean_db():
    m = MetaData()
    m.reflect(engine)
    m.drop_all(engine) 
