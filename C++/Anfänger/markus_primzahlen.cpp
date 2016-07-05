
 /*
 Erstellen Sie ein Programm, das testet ob eine gegebene Zahl eine Primzahl ist.
 */
#include <stdio.h>
#include <string.h>
#include <iostream>
#include <stdlib.h>



 using namespace std;

 int main ()
 {
    int p,zp(0),b(1);
    cout << "Gib eine Zahl ein: ";
    cin >> p;
    int i1;
    int i2;

    struct liste
    {
        int primzahl;
        struct liste *next;
    };

    const struct liste* start;
    struct liste ppuffer;
    struct liste primzahlstruct;
    primzahlstruct.next = NULL;

    start = &primzahlstruct;

    for (i1=2; i1<p; i1++)
    {
    for (i2=2; i2<i1; i2++)
     {
     if ( i1%i2 == 0)
     {
        //cout << p << " ist keine Primzahl";
        b=0;
        break;
     }

     }
     if (b)
     zp++;
     ppuffer.primzahl = i1;
     ppuffer.next = (struct liste*) malloc ( sizeof(struct liste));
     primzahlstruct.next = &ppuffer;
     &primzahlstruct = &ppuffer;
     ppuffer.next = NULL;

     b=1;
     //cout << p << " ist eine Primzahl";

    }

    cout << endl << "Dazwischen liegen: " << zp << " Primzahlen." << endl;



    for (i2=2; i2<p; i2++)
     {
     if ( p%i2 == 0)
     {
        cout << p << " ist keine Primzahl";
        return 0;
     }
     }
     cout << p << " ist eine Primzahl";

    return 0;

 }
