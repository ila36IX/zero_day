#!/usr/bin/python3
from world import Student, Course, session, Base, fake, clean_db
from sqlalchemy import delete


s = Student()
session.add(s)
session.commit()
dl = delete(Student).where(Student.id == s.id)
session.execute(dl)

session.commit()
