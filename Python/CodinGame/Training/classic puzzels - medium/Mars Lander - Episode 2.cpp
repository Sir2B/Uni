#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;


int main()
{
    int surfaceN; // the number of points used to draw the surface of Mars.
    cin >> surfaceN; cin.ignore();
    int previousY = -1;
    int previousX = -1;
    int landingY, landingX0, landingX1, landingX2;
    for (int i = 0; i < surfaceN; i++) {
        int landX; // X coordinate of a surface point. (0 to 6999)
        int landY; // Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
        cin >> landX >> landY; cin.ignore();
        if (landY == previousY){
            landingY = landY;
            landingX1 = previousX;
            landingX2 = landX;
            landingX0 = (landingX1+landingX2)/2;
            cerr << "LandingX: " << landingX1 << " - " << landingX2 << endl;
        }
        previousX = landX;
        previousY = landY;
    }


    // game loop
    while (1) {
        int X;
        int Y;
        int hSpeed; // the horizontal speed (in m/s), can be negative.
        int vSpeed; // the vertical speed (in m/s), can be negative.
        int fuel; // the quantity of remaining fuel in liters.
        int rotate; // the rotation angle in degrees (-90 to 90).
        int power; // the thrust power (0 to 4).
        cin >> X >> Y >> hSpeed >> vSpeed >> fuel >> rotate >> power; cin.ignore();

        int angel = 0;
        int thrust = 3;
        int diff = X - landingX0;
        int height = Y - landingY;

        cerr << "diff: " << diff << " height: " << height << endl;

        if (X < landingX1 || X > landingX2) //nicht über Landeplatz
        {
            if (vSpeed < 0) thrust = 4;

            //beschleunigen
            if (diff < 0) angel = -30;
            else angel = 30;

            //bremsen
            if (hSpeed > 50 || (diff < -1500 && hSpeed >= 20)) {
                angel = 15;
            }
            else if (hSpeed < -50 || (diff < 1500 && hSpeed <= -20)) {
                angel = -15;
            }
        }
        else //Landen
        {
            if (vSpeed <= -40 || (vSpeed < -10 && height < 1000) || abs(hSpeed) > 30){
                thrust = 4;
            } 

            if (hSpeed <= -10) angel = -45;
            else if (hSpeed >= 10) angel = 45;
            if (height < 250) angel = 0;
        }
        if (vSpeed <= -40) angel = 0;

        // rotate power. rotate is the desired rotation angle. power is the desired thrust power.
        cout << angel << " " << thrust << endl;
    }
}