from db.db import Database
from flask import Flask, render_template, make_response, Response, request

app = Flask(__name__)

@app.route("/")
def index() -> str:
    return render_template("index.html")

@app.route("/api/holidays", methods=["GET"])
def serve_holidays() -> Response:
    if (location := request.args.get("location")) is None:
        return make_response("oh no", 400)

    with Database() as db:
        holidays = db.get_holidays_by_location(location)

    return make_response(holidays, 200)

@app.route("/api/bookings/new", methods=["POST"])
def recive_booking() -> Response:
    print(request.get_json())

    return make_response({"all": "ok"}, 200)

if __name__ == "__main__":
    app.run(debug=True)