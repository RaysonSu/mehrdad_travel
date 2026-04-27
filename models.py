from __future__ import annotations

from datetime import date, datetime
from dataclasses import dataclass

@dataclass
class Holiday:
    holiday_id: str
    location: str
    departure_date: date
    duration: int
    outbound_journey_id: str
    return_journey_id: str

    # def as_dict(self) -> dict[str, str]:
    #     return {
    #         "duration": str(self.duration),
    #         "holiday_id": self.holiday_id,
    #         "location": self.location,
    #         "departure_date": date.strftime(self.departure_date, "%d/%m/%Y"),
    #     }

    # @staticmethod
    # def from_dict(dictionary: dict[str, str | int]) -> Holiday:
    #     return Holiday(
    #         str(dictionary["holiday_id"]),
    #         str(dictionary["location"]),
    #         datetime.strptime(str(dictionary["departure_date"]), "%Y-%m-%d"),
    #         int(dictionary["duration"]),
    #         str(dictionary["outbound_journey_id"]),
    #         str(dictionary["return_journey_id"])
    #     )
    
    # @property
    # def departure_date_str(self) -> str:
    #     return datetime.strftime(self.departure_date, "%Y-%m-%d")

@dataclass
class Customer:
    customer_id: str
    forename: str
    surname: str
    telephone: str

@dataclass
class Booking:
    booking_id: str
    customer_id: str
    holiday_id: str
    num_guests: int

@dataclass
class Flight:
    airline: str
    flight_number: str
    departure_time: datetime
    duration: int

