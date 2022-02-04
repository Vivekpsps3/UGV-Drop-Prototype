from find_drop import *

def main():
    lat = 0
    lon = 0
    alt = 100
    velocity = 10
    heading = 0
    windSpeed = 0
    windHeading = 0
    lat, lon = find_drop(lat, lon, alt, velocity, heading, windSpeed, windHeading)
    print(lat, lon)
    return 0

if __name__ == "__main__":
    main()