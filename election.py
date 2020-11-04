import requests
import urllib.request
import time
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com/interactive/2020/11/03/us/elections/results-president.html'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

score_tracker = []
swing_electoral = {
    "PA": 20, 
    "TX": 38, 
    "WI": 10, 
    "OH": 18, 
    "NC": 15, 
    "NH": 4, 
    "NV": 6, 
    "MI": 16, 
    "IA": 6, 
    "GA": 16, 
    "FL": 29, 
    "AZ": 11,
    "AB": 9, 
    "AL": 3,
    "AK": 6,
    "CA": 55,
    "CO": 9,
    "CT": 7,
    "DE": 3,
    "District of Columbia": 3,
    "HI": 4,
    "ID": 4,
    "IL": 20,
    "IN": 11,
    "KS": 6,
    "KY": 8,
    "LA": 8,
    "ME": 4,
    "MD": 10,
    "MA": 11,
    "MS": 6,
    "MO": 10,
    "NE": 5,
    "NJ": 14,
    "NM": 5,
    "NY": 29,
    "ND": 3,
    "OK": 7,
    "OR": 7,
    "RI": 4,
    "SC": 9,
    "SD": 3,
    "TN": 11,
    "UT": 6,
    "VE": 3, 
    "VA": 13, 
    "WA": 12, 
    "WV": 5, 
    "WI": 10, 
    "WY": 3
    }

for line in soup.findAll('div', attrs={'class': 'e-count-label'}):
    score_tracker.append(line.text)

print(f"Biden:\t\t{score_tracker[0]}")
print(f"Trump:\t\t{score_tracker[1]}")
print(f"Remaining:\t{score_tracker[2]}")
print('\n')

while True:
    operation = input('add or sub State: ')
    if(operation == 'add'):
        candidate = input('Candidate: ')
        if candidate == 'Trump':
            state = input('Swing State Abbreviation: ')
            score_tracker[1] = int(score_tracker[1]) + swing_electoral[state]
            print(f"[ESTIMATE] Trump:\t\t{score_tracker[1]}")
        elif candidate == 'Biden':
            state = input('Swing State Abbreviation: ')
            score_tracker[1] = int(score_tracker[0]) + swing_electoral[state]
            print(f"[ESTIMATE] Biden:\t\t{score_tracker[0]}")
        else:
            break

    elif(operation == 'sub'):
        candidate = input('Candidate: ')
        if candidate == 'Trump':
            state = input('Swing State Abbreviation: ')
            score_tracker[1] = int(score_tracker[1]) - swing_electoral[state]
            print(f"[ESTIMATE] Trump:\t\t{score_tracker[1]}")
        elif candidate == 'Biden':
            state = input('Swing State Abbreviation: ')
            score_tracker[1] = int(score_tracker[0]) - swing_electoral[state]
            print(f"[ESTIMATE] Biden:\t\t{score_tracker[0]}")
        else:
            break
    else:
        break