import requests
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model import create_tables


# session.add(test_entry)
# session.commit()


# res_json = res.json()

# import pdb; pdb.set_trace()

def get_data():
    res = requests.get(
        "https://www.domain.com.au/auction-results/api/city-summary/melbourne/2020-11-21")


def get_db():
    db_string = 'postgres:///houses'
    return create_engine(db_string, echo=True)


def main():
    db = get_db()
    Session = sessionmaker(db)
    create_tables(db)


if __name__ == "__main__":
    pass
