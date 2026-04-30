from random import randint
from typing import Any
from models import Holiday
import sqlite3

from models import *


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
    
    def get_holidays_by_location(self, location: str) -> list[Holiday]:
        records = self.__cursor.execute("SELECT * FROM Holiday WHERE Location = ?", (location,)).fetchall()
        return [
            Holiday(*record)
            for record in records
        ]
    
    def get_holiday_by_id(self, holiday_id: str) -> Holiday | None:
        record = self.__cursor.execute("SELECT * FROM Holiday WHERE HolidayID = ?", (holiday_id,)).fetchone()
        
        if not record:
            return None
        else:
            return Holiday(*record)

    def get_customer_by_names(self, forename: str, surname: str) -> Customer | None:
        record = self.__cursor.execute("SELECT * FROM Customer WHERE Forename = ? AND Surname = ?", (forename, surname)).fetchone()
        
        if not record:
            return None
        else:
            return Customer(*record)
    
    def get_allergen_by_name(self, allergen_name: str) -> Allergen | None:
        pass

    def get_food_choice_by_name(self, food_choice: str) -> Food | None:
        pass

    def create_new_customer(self, forename: str, surname: str, telephone: str) -> Customer:
        pass

    def create_new_guest(self, name: str, allergens: list[Allergens], food: Food) -> Guest:
        pass

    def create_new_booking(self, customer_id: str, holiday_id: str) -> Booking:
        pass

    def process_booking(self, booking: dict[str, Any]) -> tuple[Customer, Booking, list[Guest]]:
        holiday_id = booking.get("holiday_id")
        forename = booking.get("forename")
        surname = booking.get("surname")
        telephone = booking.get("telephone")
        guests = booking.get("guests")


        if holiday_id is None:
            raise AttributeError("holiday_id was not found in post request data")
        if not isinstance(holiday_id, str):
            raise TypeError("holiday_id is not a string")
        
        if forename is None:
            raise AttributeError("forename was not found in post request data")
        if not isinstance(forename, str):


        if surname is None:
            raise AttributeError("surname was not found in post request data")
    
        if telephone is None:
            raise AttributeError("telephone was not found in post request data")
        
        if guests is None:
            raise AttributeError("guests was not found in post request data")

        holiday = self.get_holiday_by_id(holiday_id)

        if not holiday:
            raise LookupError("Holiday was not found in the database")


        customer = self.get_customer_by_names(forename, surname)
        if not customer:
            cus




if __name__ == "__main__":
    # tests
    with Database() as db:
        print(db.get_holidays_by_location("New York"))
        print(db.get_holidays_by_location("*"))

    # should see martin davies

