import json
import requests

url = "https://www.facebook.com/api/graphql/"

payload = "av=100080720348042&__aaid=0&__user=100080720348042&__a=1&__req=2x&__hs=19924.HYP%3Acomet_pkg.2.1..2.1&dpr=2&__ccg=GOOD&__rev=1015030792&__s=vsokt4%3Aojyxs8%3Atjshhs&__hsi=7393613424164877589&__dyn=7AzHK4HwkEng5K8G6EjBAg5S3G2O5U4e2C17xt3odE98K361twYwJyE24wJwpUe8hwaG1sw9u0LVEtwMw65xO2OU7m221Fwgo9oO0-E4a3a4oaEnxO0Bo7O2l2Utwqo31wiE567Udo5qfK0zEkxe2GewyDwkUe9obrwh8lwUwgojUlDw-wUwxwjFovUaU3qxWm2CVEbUGdG0HE88cA0z8c84q58jyUaUcojxK2B08-269wkopg6C13whEeE4WVU-4EdrxG1fBG2-2K2G&__csr=guMgs52i5R4gOxcIjjcBlEZiYHGG7EARtRaB95dbkJvdlHOFT8GjvEr8hqbAO5b9akSvGkyyAFyXFBBjFqWFdFcxGy9Eykxpem449KnWGC9HyehF4-CcWz-u5rBuqm-E8ojz8iUGV4UGfyeFpVpawwzUy4opgKiUrK4oa9UWUOexi3i788FEtyrwootz8foaVonCwEwk85aq4E2WwSwEwau1qwdq4982hUlwjU8oco1PEtw1920nS1Fw0nwU03W2yo0L7w6Ow5uw3j808KE1Abw0hlo0elo0aUK0IE0Ma19wrolw1Vy0IU&__comet_req=15&fb_dtsg=NAcMGhr7VTc7uvXsmKcd1fEgZJVTHdTsTUeu3qs5DrhjAIzwtzZ_SKg%3A35%3A1720595767&jazoest=25759&lsd=KDcqWcasoqCuA2N_zyfdat&__spin_r=1015030792&__spin_b=trunk&__spin_t=1721459772&fb_api_caller_class=RelayModern&fb_api_req_friendly_name=FriendingCometFriendsListPaginationQuery&variables=%7B%22count%22%3A30%2C%22cursor%22%3A%22AQHRh68fGnEn1RTahKvGvCLAnxTAGdtcPTEUr7Abulh8ktf3Rx87vg3iCZpNaZ5IJdmTl7LVRC-JHAWPZiyb8-jxNA%22%2C%22name%22%3Anull%2C%22scale%22%3A2%7D&server_timestamps=true&doc_id=4854590387990555"
headers = {
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9",
    "content-type": "application/x-www-form-urlencoded",
    "cookie": "datr=4fSMZizuJg7aMHkqxFz1Zmbe; sb=IDWOZhDCYBNTBVEDQLE90DSD; c_user=100080720348042; ps_n=1; ps_l=1; dpr=1; xs=35%3AocooDsU_h1erWw%3A2%3A1720595767%3A-1%3A15165%3A%3AAcW034lU70sEmPwPEz7evn8Uu2ZRvkFyFYNla0hG9Q; fr=1cNkhQXCcmJzzGCMR.AWVcUTZ0s9pTsyBmJYRlPohPAD0.Bmm2KI..AAA.0.0.Bmm2Q8.AWWzbjMFYn8; presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1721459775960%2C%22v%22%3A1%7D; wd=1512x670",
    "origin": "https://www.facebook.com",
    "priority": "u=1, i",
    "referer": "https://www.facebook.com/friends/list",
    "sec-ch-prefers-color-scheme": "light",
    "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    "sec-ch-ua-full-version-list": '"Not/A)Brand";v="8.0.0.0", "Chromium";v="126.0.6478.127", "Google Chrome";v="126.0.6478.127"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": '""',
    "sec-ch-ua-platform": '"macOS"',
    "sec-ch-ua-platform-version": '"14.5.0"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "x-asbd-id": "129477",
    "x-fb-friendly-name": "FriendingCometFriendsListPaginationQuery",
    "x-fb-lsd": "KDcqWcasoqCuA2N_zyfdat",
}

response = requests.request("POST", url, headers=headers, data=payload)

with open('fb_friends.json', 'w', encoding='utf-8') as f:
    json.dump(json.loads(response.text), f, ensure_ascii=False, indent=4)
