'''

If a runner runs 10 miles in 30 minutes and 30 seconds,
What is his/her average speed in kilometers per hour? (Tip: 1 mile = 1.6 km)

'''

def get_kph(distance, time):
    """take distance (kilometers) and time (minutes) and return speed in kilometers/hour"""

    hours = time / 60
    kph = distance / hours
    return int(kph)

kilometers = 10 * 1.6
minutes = 30.5

print(get_kph(kilometers, minutes))
