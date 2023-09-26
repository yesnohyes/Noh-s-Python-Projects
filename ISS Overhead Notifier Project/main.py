import requests
import datetime as dt
import smtplib
import time

MY_LAT = 1.439470
MY_LONG = 103.801310
MY_EMAIL = "imnotnoh@gmail.com"
MY_PASSWORD = "tcoefnecxbdvbgau"


def check_position():
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    print(iss_response.status_code)
    iss_response.raise_for_status()
    latitude = float(iss_response.json()["iss_position"]["latitude"])
    longitude = float(iss_response.json()["iss_position"]["longitude"])

    if MY_LAT-5 <= latitude <= MY_LAT+5 and longitude == MY_LONG:
        return True


def check_time():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data['results']['sunrise'].split("T")[1].split(":")[0])+8
    sunset = int(data['results']['sunset'].split("T")[1].split(":")[0])+8

    hour_now = dt.datetime.now().hour

    if hour_now >= sunset or hour_now <= sunrise:
        return True


if check_position() and check_time():
    time.sleep(60)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        # TODO: to encypt the email and secure the connection
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:ISS_SATELLITE\n\nLOOK UP AT THE SKY!!!!")