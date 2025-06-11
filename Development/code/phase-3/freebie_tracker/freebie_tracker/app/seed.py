# app/seed.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base, Dev, Company, Freebie

engine = create_engine('sqlite:///freebies.db')
Session = sessionmaker(bind=engine)
session = Session()

def seed():
    print("Seeding data...")
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    devs = [
        Dev(name="Kelvin"),
        Dev(name="Ada"),
        Dev(name="Grace"),
        Dev(name="Linus")
    ]

    companies = [
        Company(name="OpenAI", founding_year=2015),
        Company(name="Google", founding_year=1998),
        Company(name="Netflix", founding_year=1997)
    ]

    freebies = [
        companies[0].give_freebie(devs[0], "T-Shirt", 25),
        companies[1].give_freebie(devs[0], "Laptop Sticker", 5),
        companies[0].give_freebie(devs[1], "Notebook", 10),
        companies[2].give_freebie(devs[2], "Socks", 15),
        companies[0].give_freebie(devs[0], "Pen", 2)
    ]

    session.add_all(devs + companies + freebies)
    session.commit()
    print("Seeding complete.")

if __name__ == "__main__":
    seed()
