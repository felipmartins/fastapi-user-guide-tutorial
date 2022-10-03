from typing import Optional
from sqlmodel import Field, SQLModel, create_engine, Session, select


class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    secret_name: str
    age: Optional[int] = None

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def create_heroes():
    hero_1 = Hero(name="Deadpond", secret_name="Dive Wilson")
    hero_2 = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")
    hero_3 = Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48)
    hero_4 = Hero(name="Tarantula", secret_name="Natalia Roman-on", age=32)
    hero_5 = Hero(name="Black Lion", secret_name="Trevor Challa", age=35)
    hero_6 = Hero(name="Dr. Weird", secret_name="Steve Weird", age=36)
    hero_7 = Hero(name="Captain North America", secret_name="Esteban Rogelios", age=93)

    with Session(engine) as session:
        session.add(hero_1)
        session.add(hero_2)
        session.add(hero_3)
        session.add(hero_4)
        session.add(hero_5)
        session.add(hero_6)
        session.add(hero_7)

        session.commit()

def select_heroes():
    with Session(engine) as session:
        statement = select(Hero)
        results = session.exec(statement)
        for hero in results:
            print(hero.name)

def select_specific_hero(hero_name: str):
    with Session(engine) as session:
        statement = select(Hero).where(Hero.name == hero_name)
        results = session.exec(statement)
        for hero in results:
            print(hero)

def select_diffenrent_heroes(hero_name: str):
    with Session(engine) as session:
        statement = select(Hero).where(Hero.name != hero_name)
        results = session.exec(statement)
        for hero in results:
            print(hero)

def select_over_35_heroes():
    with Session(engine) as session:
        statement = select(Hero).where(Hero.age >= 35)
        results = session.exec(statement)
        for hero in results:
            print(hero)


def main():
    create_db_and_tables()
    create_heroes()
    select_heroes()
    select_specific_hero("Spider-Boy")
    select_diffenrent_heroes("Spider-Boy")
    select_over_35_heroes()

if __name__ == "__main__":
    main()
