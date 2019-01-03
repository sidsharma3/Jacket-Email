import requests
import smtplib

conn = smtplib.SMTP('smtp.gmail.com', 587)
conn.ehlo()
conn.starttls()
conn.login('email', 'password')
personemail = input('what is your email?\n')

city = input('City Name?\n')
url = 'http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q=' + city
json_data = requests.get(url).json()
kelvin = json_data['main']['temp']

if (round(kelvin - 273)) >= 0:
    print('jacket')
    conn.sendmail('email', personemail, 'Subject: I sent this from python\n\nDear,\n wear jacket.\n')
else:
    print('no jacket')
    conn.sendmail('email', personemail, 'Subject: I sent this from python\n\nDear,\n dont wear jacket.\n')

    
