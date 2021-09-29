from ics import Calendar
import requests

def get_all_dates(month, grp_english):
    url = 'https://calendar.google.com/calendar/ical/vkcaks7nqiiub3gp6a24po6gfk%40group.calendar.google.com/public/basic.ics'
    c = Calendar(requests.get(url).text)
    all_events = []
    print(grp_english)
    for event in c.events:
        if event.begin.month == month: # le bon mois
            if 'Ang' in event.name:  # groupe anglais
                if '(grp ' + grp_english in event.name:
                    all_events.append(event)
            elif 'seulement FI' not in event.name and 'Férié' not in event.name and 'Interruption pédagogique' not in event.name:  # osef des FI & jour fériés
                all_events.append(event)
    all_events.sort()
    return all_events
