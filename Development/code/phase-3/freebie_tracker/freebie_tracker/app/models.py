# app/models.py

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Dev(Base):
    __tablename__ = 'devs'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)

    freebies = relationship('Freebie', back_populates='dev', cascade='all, delete-orphan')

    def __repr__(self):
        return f"<Dev(name='{self.name}')>"

    def received_one(self, item_name):
        return any(freebie.item_name == item_name for freebie in self.freebies)

    def give_away(self, other_dev, freebie):
        if freebie in self.freebies:
            freebie.dev = other_dev
        else:
            raise ValueError(f"{self.name} doesn't own this freebie!")

    def all_freebie_items(self):
        return [freebie.item_name for freebie in self.freebies]

    def total_freebie_value(self):
        return sum(f.value for f in self.freebies)


class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    founding_year = Column(Integer)

    freebies = relationship('Freebie', back_populates='company', cascade='all, delete-orphan')

    def __repr__(self):
        return f"<Company(name='{self.name}')>"

    def give_freebie(self, dev, item_name, value):
        new_freebie = Freebie(item_name=item_name, value=value, dev=dev, company=self)
        return new_freebie

    def biggest_fan(self):
        dev_counts = {}
        for freebie in self.freebies:
            dev = freebie.dev
            dev_counts[dev] = dev_counts.get(dev, 0) + 1
        return max(dev_counts, key=dev_counts.get, default=None)

    def average_freebie_value(self):
        values = [f.value for f in self.freebies]
        return round(sum(values) / len(values), 2) if values else 0


class Freebie(Base):
    __tablename__ = 'freebies'

    id = Column(Integer, primary_key=True)
    item_name = Column(String, nullable=False)
    value = Column(Integer, nullable=False)

    dev_id = Column(Integer, ForeignKey('devs.id'))
    company_id = Column(Integer, ForeignKey('companies.id'))

    dev = relationship('Dev', back_populates='freebies')
    company = relationship('Company', back_populates='freebies')

    def __repr__(self):
        return f"<Freebie(item='{self.item_name}', value={self.value})>"

    def print_details(self):
        print(f"{self.dev.name} owns a {self.item_name} from {self.company.name}.")
