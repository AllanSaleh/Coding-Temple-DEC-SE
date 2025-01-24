from sqlalchemy import create_engine
from sqlalchemy import String, DateTime, func, select, Date, ForeignKey, Table, Column
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session, relationship
from datetime import date
from typing import List

# One to Many relationship
# one Instructor can be on many Workshops 

# Many to Many relationship
# Where many students can attend many workshops, and many workshops can be attended by many students.

engine = create_engine('mysql+mysqlconnector://root:CodingTemple@localhost/coding_temple')

class Base(DeclarativeBase):
    pass

class Workshop(Base):
    __tablename__ = 'workshops'

    workshop_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30), nullable=False)
    date_: Mapped[date] = mapped_column(Date, nullable=False)
    instructor_id: Mapped[int] = mapped_column(ForeignKey('sqlalchemy_instructors.instructor_id'))
    created_at = mapped_column(DateTime, default=func.now())
    updated_at = mapped_column(DateTime, default=func.now(), onupdate=func.now())

    instructors: Mapped["SQLAlchemy_Instructors"] = relationship(back_populates='workshops')
    students: Mapped[List["SQLAlchemy_Students"]] = relationship(back_populates='workshops', secondary='student_workshops')

class SQLAlchemy_Instructors(Base):
    __tablename__= 'sqlalchemy_instructors'

    instructor_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    department: Mapped[str] = mapped_column(String(100))
    created_at = mapped_column(DateTime, default=func.now())
    updated_at = mapped_column(DateTime, default=func.now(), onupdate=func.now())

    workshops: Mapped[List["Workshop"]] = relationship(back_populates='instructors')

class SQLAlchemy_Students(Base):
    __tablename__= 'sqlalchemy_students'

    student_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    enrollement_date: Mapped[date] = mapped_column(Date)
    created_at = mapped_column(DateTime, default=func.now())
    updated_at = mapped_column(DateTime, default=func.now(), onupdate=func.now())

    workshops: Mapped[List["Workshop"]] = relationship(back_populates="students", secondary='student_workshops')

student_workshops = Table(
    "student_workshops",
    Base.metadata,
    Column("workshop_id", ForeignKey('workshops.workshop_id')),
    Column("student_id", ForeignKey('sqlalchemy_students.student_id'))
)

Base.metadata.create_all(engine)

session = Session(engine)

Yessica = SQLAlchemy_Instructors(name="Yessica", department="SSM")

Whiteboard_Wednesdays = Workshop(name="Whiteboard", date_="2025-01-22")
Codewars_Saturday = Workshop(name="Codewars", date_="2025-01-25")

Bill = SQLAlchemy_Students(name="Bill", enrollement_date="2025-01-23")
Ted = SQLAlchemy_Students(name="Ted", enrollement_date="2025-01-23")
Bill.workshops.append(Whiteboard_Wednesdays)
Bill.workshops.append(Codewars_Saturday)
Ted.workshops.append(Whiteboard_Wednesdays)

Whiteboard_Wednesdays.students.append(Bill)
Whiteboard_Wednesdays.students.append(Ted)
Codewars_Saturday.students.append(Bill)

Yessica.workshops.append(Whiteboard_Wednesdays)
Yessica.workshops.append(Codewars_Saturday)

# session.add(Yessica)
# session.add(Whiteboard_Wednesdays)
# session.add(Codewars_Saturday)
# session.add(Bill)
# session.add(Ted)
# session.commit()

# query = select(SQLAlchemy_Instructors).where(SQLAlchemy_Instructors.name == "Yessica")
# yessica_workshops = session.execute(query).scalars().all()
# print(yessica_workshops)

# query = select(Workshop)
# all_workshops = session.execute(query).scalars().all()
# print(all_workshops)
# for workshop in all_workshops:
#     print(workshop.name)
#     print(workshop.instructors.name)

# for workshop in yessica_workshops:
#     print(workshop.name)
#     print(workshop.workshops[1].name)

query = select(student_workshops)
all_workshops = session.execute(query).scalars().all()
print(all_workshops)

for workshop in Bill.workshops:
    print(workshop.name, workshop.date_, workshop.instructors.workshops)


session.close()