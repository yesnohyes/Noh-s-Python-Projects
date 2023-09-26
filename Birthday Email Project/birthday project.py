import random
import smtplib
import pandas as pd
import datetime as dt


MY_EMAIL = "imnotnoh@gmail.com"
MY_PASSWORD = "tcoefnecxbdvbgau"

NOW = dt.datetime.today()
DAY = NOW.day
MONTH = NOW.month

birthday_data = pd.read_csv("birthdays.csv")
birthday_list = birthday_data.to_dict(orient='records')


for person in birthday_list:
    if person['month'] == MONTH and person['day'] == DAY:
        number = random.randint(1, 3)
        with open(f"letter_templates/letter_{number}.txt") as text:
            birthday_letter = text.read()
            # replace comes as an output hence you need to save it under the same variable
            birthday_letter = birthday_letter.replace("[NAME]", person['name'])
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                # TODO: to encypt the email and secure the connection
                connection.starttls()
                connection.login(user=MY_EMAIL, password=MY_PASSWORD)
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=person['email'],
                    msg=f"Subject:Happy Birthday!\n\n{birthday_letter}")

