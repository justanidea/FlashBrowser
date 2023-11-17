import sys
import requests

primary_cookie = sys.argv[1]
cookies={"phoenixUser":primary_cookie}
url="https://galaxylifegame.net/game"
found: bool = False

response = requests.get(url=url, cookies=cookies)
for iteration in response.history:
    if 'set-cookie' in iteration.headers:
        if len(iteration.headers["set-cookie"].split("session=")) == 2:
            secondary_cookie = iteration.headers["set-cookie"].split("session=")[1].split(";")[0]
            found = True
            command = f"/set_cookie cookie:{secondary_cookie}"
            print(secondary_cookie)
            