from mvg_api import *

class Departure():
    def __init__(self, dep_raw):
        self.line = dep_raw['label']
        self.to = dep_raw['destination']
        self.minutes = dep_raw['departureTimeMinutes']
        self.delay = dep_raw['delay']
        self.is_delayed = dep_raw['delay'] != 0

        time = dep_raw['departureTime']
        timestamp = time / 1000
        self.at = datetime.datetime.fromtimestamp(timestamp).strftime("%H:%M")

    def __str__(self):
        return f'{self.line} to {self.to}: at {self.at} in {self.minutes}min with delay {self.delay}min {self.is_delayed}'

def departures(depature, destination):
    station = Station(depature)
    departures_raw = station.get_departures()

    return list(
        map(lambda d: Departure(d),
            list(
                filter(lambda dr: destination in dr['destination'], departures_raw))
            )
    )

def departure_eching():
    return departures("Eching", "Flughafen")

def departure_neufahrn():
    return departures("Neufahrn", "Leuchtenberg")
