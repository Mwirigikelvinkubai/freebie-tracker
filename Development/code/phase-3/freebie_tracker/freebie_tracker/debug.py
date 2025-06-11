# debug.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base, Dev, Company, Freebie

# Setup engine and session (match your seed.py config)
engine = create_engine('sqlite:///freebies.db')
Session = sessionmaker(bind=engine)
session = Session()

def main():
    # Fetch a Dev and print all their freebies
    dev = session.query(Dev).filter_by(name="Kelvin").first()
    if dev:
        print(f"Developer: {dev.name}")
        print("Freebies owned:")
        for freebie in dev.freebies:
            freebie.print_details()
        print(f"Total value of freebies: ${dev.total_freebie_value()}")
        print(f"Has Kelvin received 'Pen'? {dev.received_one('Pen')}")

    # Transfer a freebie to another Dev
    ada = session.query(Dev).filter_by(name="Ada").first()
    freebie_to_give = dev.freebies[0] if dev and dev.freebies else None
    if freebie_to_give and ada:
        print(f"\nGiving away '{freebie_to_give.item_name}' from {dev.name} to {ada.name}")
        dev.give_away(ada, freebie_to_give)
        session.commit()

    # Check updated freebies for Ada
    print(f"\nAfter transfer, {ada.name} owns:")
    for freebie in ada.freebies:
        freebie.print_details()

    # Company info & biggest fan
    company = session.query(Company).filter_by(name="OpenAI").first()
    if company:
        print(f"\nCompany: {company.name}")
        print(f"Biggest fan: {company.biggest_fan()}")
        print(f"Average freebie value: ${company.average_freebie_value()}")

if __name__ == "__main__":
    main()
