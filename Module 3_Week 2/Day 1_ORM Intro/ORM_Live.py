from sqlalchemy import create_engine
from sqlalchemy import String, DateTime, func, select, Date
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
from datetime import date

engine = create_engine('mysql+mysqlconnector://root:CodingTemple@localhost/coding_temple')

class Base(DeclarativeBase):
    pass

class Workshop(Base):
    __tablename__ = 'workshops'

    workshop_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30), nullable=False)
    date_: Mapped[date] = mapped_column(Date, nullable=False)
    created_at = mapped_column(DateTime, default=func.now())
    updated_at = mapped_column(DateTime, default=func.now(), onupdate=func.now())

Base.metadata.create_all(engine)

session = Session(engine)

Whiteboard = Workshop(name="Codewars", date_="2025-01-22")
# session.add(Whiteboard)
# session.commit()

query = select(Workshop)
all_workshops = session.execute(query).scalars().all()
# for workshop in all_workshops:
#     print(workshop.name, workshop.date_, workshop.workshop_id, workshop.created_at)

whiteboard_only = session.query(Workshop).filter(Workshop.name.like('%White%')).all()
for workshop in whiteboard_only:
    print(workshop.name, workshop.date_, workshop.workshop_id, workshop.created_at)

query = select(Workshop).where(Workshop.workshop_id == 1)
specific_workshop = session.execute(query).scalars().first()

specific_workshop.name = 'Codewars'

session.commit()

for workshop in all_workshops:
    print(workshop.name, workshop.date_, workshop.workshop_id, workshop.created_at)

query = select(Workshop).where(Workshop.workshop_id == 3)
specific_workshop = session.execute(query).scalars().first()

session.delete(specific_workshop)
session.commit()

session.close()