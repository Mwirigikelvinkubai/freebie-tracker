# Freebie Tracker


A Phase 3 Code Challenge project built with Python and SQLAlchemy.



Freebie Tracker is an app that helps developers keep track of the promotional items (freebies) they receive from different tech companies during events like hackathons and conferences.

The application models real-world relationships between developers, companies, and the freebies they exchange using SQLAlchemy ORM.

 Structure

freebie_tracker/
├── app/
│ ├── init.py
│ ├── models.py
│ ├── db.py
│ └── seed.py
├── migrations/
│ └── xxxx
├── debug.py
├── main.py
├── .gitignore
└── README.md

markdown
Copy
Edit

Features (to be implemented)

- Track companies and their founding years.
- Manage developers and the freebies they receive.
- Relationship modeling:
  - Companies have many freebies.
  - Developers have many freebies.
  - Freebies belong to both companies and developers.
- Aggregation methods such as:
  - Transfer freebies between devs.
  - Track which devs received which items.
  - Identify the oldest company.

