from __future__ import annotations

from datetime import date, datetime
from dataclasses import dataclass

from typing import Any

@dataclass
class Holiday:
    holiday_id: str
    location: str
    departure_date: date
    duration: int
    outbound_journey_id: str
    return_journey_id: str

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
class Guest:
    pass

@dataclass
class Flight:
    airline: str
    flight_number: str
    departure_time: datetime
    duration: int

@dataclass
class Allergen:
    allergen_id: str

class 