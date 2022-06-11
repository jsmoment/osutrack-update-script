from requests import post
from time import sleep

# standard user list
users = {
    "jotsa": 11423613,
    "SeniorMcFluff_": 13608087,
    "Andii286": 14689295,
    "akacz2115": 17226323,
    "nextu": 14408373,
    "tortori-": 27985148
}

# taiko user list
taiko = {
    "tortori-": 27985148
}

# 0 = standard
def update(user):
    post(f"https://osutrack-api.ameo.dev/update?user={user}&mode=0")

# 1 = taiko
def taikoupdate(user):
    post(f"https://osutrack-api.ameo.dev/update?user={user}&mode=1")

# make the requests for standard updates
for x in users:
    update(users[x])
    sleep(0.2)
# make the requests for taiko updates
for x in taiko:
    taikoupdate(taiko[x])
    sleep(0.2)
