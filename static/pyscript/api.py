from pyodide.http import pyfetch

def sanitise(string: str) -> str:
    # TODO: do this properly
    return string

async def get_request_holidays(location: str) -> str:
    response = await pyfetch(f"/api/holidays?location={sanitise(location)}")   
    data = await response.json()

    print(f"{location} => {data}")

    return data
