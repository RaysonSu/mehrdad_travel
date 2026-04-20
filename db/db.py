from random import randint
from typing import Any
import sqlite3


class Database:
    def __enter__(self) -> Database:
        self.__conn = sqlite3.connect("./db/holidays.db")
        self.__cursor = self.__conn.cursor()

        return self

    def __exit__(self, *args) -> None:
        self.__conn.close()
    
    def add_new_customer(self, forename: str, surname: str, telephone: str):
        id_ = forename[0] + surname[:2].upper() + str(randint(111, 999))
        self.__cursor.execute(f"INSERT INTO Customer VALUES ('{id_}', '{forename}', '{surname}', '{telephone}')")
        self.__conn.commit()

    def get_all_customers(self) -> list[list[Any]]:    
        records = self.__cursor.execute("SELECT * FROM Customer").fetchall()
        return records
    
    def get_holidays(self, location: str) -> list[list[Any]]:
        records = self.__cursor.execute("SELECT * FROM Holiday WHERE Location = ?", (location,)).fetchall()
        return records

if __name__ == "__main__":
    # tests
    with Database() as db:
        print(db.get_holidays("New York"))
        print(db.get_holidays("*"))

    # should see martin davies

