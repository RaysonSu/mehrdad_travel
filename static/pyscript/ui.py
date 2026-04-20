from pyscript import document, when

from api import get_request_holidays

@when("click", ".search-cta")
async def click_go(event) -> None:
    location: str = document.getElementById("dest").value
    holidays = await get_request_holidays(location)

    print(holidays)

# go_button = document.getElementsByClassName("search-cta")[0]

