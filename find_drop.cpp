#include <stdio.h>
#include <math.h>
#include <iostream>
#include <cmath>
using namespace std;

void find_drop(float lat, float lon, float alt, float velocity, float heading, float windSpeed, float windHeading)
{

    windHeading = windHeading * (M_PI/ 180);
    heading = heading * (M_PI / 180);

    float g = 9.81;
    float rEarth = 6378.1;

    float pullHeight = 12.192;
    float freeFall = alt - pullHeight;
    float freeFTime = sqrt((2 * freeFall) / g);

    float xVel = velocity * cos(heading);
    float yVel = velocity * sin(heading);
    float dX = xVel * freeFTime;
    float dY = yVel * freeFTime;

    float parVel = 5.1816;
    float parTime = pullHeight / parVel;
    float xWVel = windSpeed * cos(windHeading);
    float yWVel = windHeading * sin(windHeading);
    dX += xWVel * parTime;
    dY += yWVel * parTime;

    //Add 1.5 seconds of extra motion

    //Coordinate changing and returning
    float latKm = 111111.0 + (1.0/ 9.0);
    float longKm = (M_PI / 180) * rEarth * cos(lon * M_PI / 180) * 1000;
    lon = dX / latKm + lon;
    lat = dY / longKm + lat;
}
// Airstrip latitude : 38.147250
// Airstrip Longitude : -76.426444
int main(int argc, char *argv[]) {
    float lat = 12.112;
    float lon = 12.112;
    float alt = 100.394;
    float velocity = 10;
    float heading = 45.8;
    float windSpeed = 12.12;
    float windHeading = 12.12;
    find_drop(lat, lon, alt, velocity, heading, windSpeed, windHeading);
    return 0;
}
