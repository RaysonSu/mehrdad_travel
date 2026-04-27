from pyscript import document, when
from json import loads
from typing import Any

from api import get_request_holidays, post_request_booking
from dto import parse_booking, parse_guest

@when("click", ".search-cta")
async def click_go(event) -> None:
    location: str = document.getElementById("dest").value
    holidays = await get_request_holidays(location)

    tag = document.getElementById("trip")

    tag.innerHTML = ""

    for holiday in loads(holidays):
        holiday_id = holiday["holiday_id"]
        location = holiday["location"]
        departure_date = holiday["departure_date"]
        duration = holiday["duration"]

        opt = document.createElement("option")
        opt.value = holiday_id
        opt.text = f"Go to {location} on {departure_date} for {duration} day(s)"
        
        tag.add(opt)
    
    form = document.getElementById("booking-form")
    for tag in form.querySelectorAll("input, select, button"):
        tag.disabled = False

@when("click", "#book")
async def create_booking(event) -> None:
    customer_name = document.getElementById(f"cust-name").value
    telephone = document.getElementById(f"cust-tel").value
    holiday = document.getElementById(f"trip").value
    guest = read_guest(1)
    
    booking = parse_booking(customer_name, telephone, holiday, [guest])

    feedback = await post_request_booking(booking)

def read_guest(id_: int) -> dict[str, Any]:
    guest_name = document.getElementById(f"guest{id_}-name").value
    
    allergies: list[str] = []
    allergies_tag = document.getElementById(f"guest{id_}-allergies")
    for allergen in allergies_tag.getElementsByTagName("input"):
        if allergen.checked:
            allergies.append(allergen.value)
    

    meal = document.getElementById(f"guest{id_}-meal").value

    return parse_guest(guest_name, allergies, meal)