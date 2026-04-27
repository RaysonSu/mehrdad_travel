from typing import Any
from json import dumps

from pyodide.http import pyfetch

def sanitise(string: str) -> str:
    sanitised = ""
    for char in string:
        if char in "{}[]%\'\"&?":
            sanitised += f"%{hex(ord(char))[2:]}"
        else:
            sanitised += char
    
    return sanitised

async def get_request_holidays(location: str) -> str:
    response = await pyfetch(f"/api/holidays?location={sanitise(location)}")   
    data = await response.text()

    return str(data)

async def post_request_booking(booking: dict[str, Any]) -> dict[str, Any]:
    print(booking)

    response = await pyfetch(
        f"/api/bookings/new", 
        method="POST", 
        headers={"Content-Type": "application/json"},
        body=dumps(booking)
    )
    
    data = await response.json()

    return data

