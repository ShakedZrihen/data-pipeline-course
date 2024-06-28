
import random
import json
from datetime import datetime, timedelta
import os

def generate_random_time():
    base_time = datetime.strptime('00:00', '%H:%M')
    random_minutes = random.randint(0, 1439)  # 1440 minutes in a day
    random_time = base_time + timedelta(minutes=random_minutes)
    return random_time.strftime('%H:%M')

def generate_random_content():
    headlines = [
        "Prime Minister to hold coalition meeting on Sunday",
        "Military eliminates Hezbollah operatives in southern Lebanon",
        "Reports of roadblocks at Acre due to security situation are fake news",
        "Fire breaks out in Kibbutz Kfar Etzion, spreads to Etzion Brigade headquarters",
        "Sirens in Upper Galilee",
        "Minister to the Chief of Staff: 'We didn't go to sleep on October 6th'",
        "Military finds game in Rafah educating Gaza children to terrorism",
        "Eilat: Man in his 50s in serious condition after drowning in the sea",
        "Kremlin: 'Putin did not wake up to watch the US presidential debate'",
        "Supreme Court: State must respond within a month to the petition on the failure to establish a state inquiry committee",
        "Deputy Chief of Staff holds professional visit to US military this week",
        "Yehuda Deri, brother of Shas chairman and member of the rabbinical council, hospitalized in serious condition",
        "Report of incident in the Red Sea, northwest of Yemen",
        "Mitzpe Ramon: Pictures of hostages were vandalized and torn at the municipal pool",
        "Hadera: Man in his 30s seriously injured by gunfire",
        "Thomas Friedman: 'I watched the debate and cried, Biden must withdraw from the race'",
        "Death of one of the injured in the car explosion in Herzliya confirmed",
        "Sirens in Western Galilee",
        "29-year-old man seriously injured in motorcycle accident",
        "Presidential elections in Iran begin",
        "Report: US invites Arab and Israeli foreign ministers to NATO summit",
        "Survey: 67% believe Trump won the debate",
        "Military attacked Hezbollah targets in southern Lebanon overnight",
        "Democratic party very worried: 'We need to convince Biden to withdraw'",
        "Weather forecast: heatwave across the country, high humidity along the coast",
        "Sergeant Eyal Shines, 19, a fighter in the Nahal Brigade, fell in battle in southern Gaza Strip",
        "Trump attacked Biden on his performance: 'I did excellent cognitive tests - he won't pass'",
        "Biden: 'You had sex with a porn star while your wife was pregnant'; Trump: 'Didn't happen'",
        "Trump: 'Hamas wouldn't have invaded Israel if I were president because Iran would be bankrupt'"
    ]
    
    content = {}
    for _ in range(30):
        time = generate_random_time()
        headline = random.choice(headlines)
        content[time] = headline
    
    return content

def save_content_to_file(content, date, path='.'):
    date_str = date.strftime('%Y-%m-%d')
    filename = os.path.join(path, f"{date_str}.json")
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(content, f, ensure_ascii=False, indent=4)

