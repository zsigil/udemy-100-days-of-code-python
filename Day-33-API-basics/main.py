import requests
import time
import datetime as dt


def positions_are_close(pos1, pos2):
    if abs(pos1[0]-pos2[0]) <= 5 and abs(pos1[1]-pos2[1]) <= 5:
        return True
    else:
        return False


def is_dark(current_hour, sunset_hour, sunrise_hour):
    if current_hour >= sunset_hour or current_hour <= sunrise_hour:
        return True
    else:
        return False


url = "http://api.open-notify.org/iss-now.json"

res = requests.get(url=url)
res.raise_for_status()

data = res.json()
iss_pos = (float(data['iss_position']['latitude']),
           float(data['iss_position']['longitude']))
print(iss_pos)

# time.sleep(3)

my_pos = (47.6008, 19.3605)
sun_url = f"https://api.sunrise-sunset.org/json?lat={my_pos[0]}&lng={my_pos[1]}&formatted=0"


res_sun = requests.get(sun_url)
res_sun.raise_for_status()
sun_data = res_sun.json()

sunrise = sun_data["results"]["sunrise"]
sunset = sun_data["results"]["sunset"]

sunrise_hour = int(sunrise.split('T')[1].split(':')[0])
sunset_hour = int(sunset.split('T')[1].split(':')[0])
current_time_hour = dt.datetime.now().hour


# if iss is close (+/- 5 degrees)
# and dark
if positions_are_close(my_pos, iss_pos) and is_dark(current_time_hour, sunset_hour, sunrise_hour):
    print('hey')
    # send email
