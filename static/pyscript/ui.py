from pyscript import document, when
from json import loads

from api import get_request_holidays

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
    for tag in form.getElementsByTagName("input"):
        tag.disabled = False

    for tag in form.getElementsByTagName("select"):
        tag.disabled = False

    for tag in form.getElementsByTagName("button"):
        tag.disabled = False

# go_button = document.getElementsByClassName("search-cta")[0]

