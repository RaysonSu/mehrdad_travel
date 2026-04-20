from datetime import date, datetime
from dataclasses import dataclass

@dataclass
class Holiday:
    duration: int
    holiday_id: str
    location: str
    departure_date: date

    def as_dict(self) -> dict[str, str]:
        return {
            "duration": str(self.duration),
            "holiday_id": self.holiday_id,
            "location": self.location,
            "departure_date": str(self.departure_date),
        }

    @staticmethod
    def from_dict(dictionary: dict[str, str]) -> Holiday:
        return Holiday(
            int(dictionary["duration"]),
            dictionary["holiday_id"],
            dictionary["location"],

        )

@dataclass
class Customer:
    forename: str
    surname: str
    customer_id: str
    telephone: str

@dataclass
class Booking:
    customer: Customer
    holiday: Holiday

@dataclass
class Flight:
    airline: str
    flight_number: str
    departure_time: datetime
    duration: int

