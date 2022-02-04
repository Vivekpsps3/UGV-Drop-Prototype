import math

def find_drop(lat, lon, alt, velocity, heading, windSpeed, windHeading):
    #You get information of aircraft as it is now
    '''
    :param lat: Latitude
    :param lon: Longitude
    :param alt: Altitude (meters): Height above ground(NOT SEA LEVEL ALT)
    :param velocity: m/s
    :param heading:
    :param windSpeed: m/s
    :param windHeading:
    :return:
    '''

    '''
    Coordinate system clarification
    x axis runs horizontally(from 270 to 90)
    y axis runs vertically(000 to 180)
    '''
    #Variable setup and basic conversions
    windHeading = windHeading*(math.pi/180)
    heading = heading * (math.pi / 180)
    g = 9.81
    rEarth = 6378.1

    #Falls (without air resistance)
    pullHeight = 12.192 #40 feet in meters
    freeFall = alt - pullHeight
    freeFTime = math.sqrt((2*freeFall)/g)

    xVel = velocity * math.cos(heading)
    yVel = velocity * math.sin(heading)
    dX = xVel * freeFTime
    dY = yVel * freeFTime

    #Accounting for parachute drop time
    parVel = 5.1816 #Drop rate of UGV while parachute is open
    parTime = pullHeight/parVel
    xWVel = windSpeed * math.cos(windHeading)
    yWVel = windHeading * math.sin(windHeading)
    dX += xWVel * parTime
    dY += yWVel * parTime

    #Coordinate changing and returning
    latKm = 111111.111111111111111
    longKm = (math.pi/180) * rEarth * math.cos(lon*math.pi/180) * 1000
    lon += dX/latKm
    lat += dY/longKm
    return [lat, lon]
