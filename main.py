from find_drop import *
from mavsdk import System,telemetry

def main():
    drone = System()
    await drone.connect(system_address="udp://:14540")
    lat = 12.112
    lon = 12.112
    alt = 100.394
    velocity = 10
    heading = 45.8
    windSpeed = 12.12
    windHeading = 12.12
    lat, lon = find_drop(lat, lon, alt, velocity, heading, windSpeed, windHeading)

    lat = telemetry.gps_latitude
    lon = telemetry.gps_longitude
    alt = telemetry.gps_altitude
    velocityN = telemetry.velocity_ned.north_m_s
    velocityE = telemetry.velocity_ned.east_m_s
    windSpeed = 12.12
    windHeading = 12.12
    lat, lon = find_drop(lat, lon, alt, velocityN,velocityE, heading, windSpeed, windHeading)
    print(lat, lon)

    return 0

if __name__ == "__main__":
    main()