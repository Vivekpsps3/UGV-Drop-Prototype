from find_drop import *

def main():
    lat = 12.112
    lon = 12.112
    alt = 100.394
    velocity = 10
    heading = 45.8
    windSpeed = 12.12
    windHeading = 12.12
    lat, lon = find_drop(lat, lon, alt, velocity, heading, windSpeed, windHeading)
    print(lat, lon)
    return 0

if __name__ == "__main__":
    main()