import pandas as pd
import datetime as dt
from random import randint
import smtplib

now = dt.datetime.now()
month = now.month
day = now.day
birthdate = (month, day)
my_email = ''
password = ''

birthday_data = pd.read_csv('birthdays.csv')
for i, r in birthday_data.iterrows():
    if (r.month, r.day) == birthdate:
        random_letter = randint(1, 3)
        with open(f'letter_templates/letter_{random_letter}.txt') as file:
            lines = file.read()
            lines = lines.replace('[NAME]', r['name'])

        with smtplib.SMTP('smtp.gmail.com') as gmail:
            gmail.starttls()
            gmail.login(user=my_email, password=password)
            gmail.sendmail(
                from_addr=my_email,
                to_addrs=r['email'],
                msg=f'Subject:Happy Birthday!\n\n{lines}'
            )


# 4. Send the letter generated in step 3 to that person's email address.




