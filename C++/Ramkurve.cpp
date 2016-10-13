#include <iostream>


int main ()
{
long int b=0;        
unsigned int z;
        unsigned int obergrenze;


        typedef struct
{
                int a;
struct speicher *next;
}speicher;


struct speicher *start;
struct speicher *platzalt;


start.next=platzalt;




//Abfrage wie viel Speicher belegt werden soll


std::cout << “Wie viel MB Arbeitsspeicher soll belegt werden?”<< std::endl;
std::cin >> obergrenze;
obergrenze*=1000000;                 //Umrechnung von MB zu B


std::cout << “Wie oft soll der Arbeitsspeicher zugemüllt werden?”<< std::endl;
std::cin >> z;
        
while (z!=0)
{
//Speicherbelegung
while (b<obergrenze)
{
        new struct speicher *platzneu;        //neuen Speicherplatz belegen
        platzalt.next=platzneu;        //Zeiger auf neuen Speicherplatz ausrichten
        platzalt=platzalt.next;                //Sprung zum nächsten Element
        b= b+4+1;                        //theoretisch belegten Speicher erhöhen


}
        platzneu.next=NULL;                        //Kettenende einfügen












        //Speicherfreigabe


        platzalt=start.next;
        while(platzalt.next!=NULL)
{
        platzneu=platzalt.next;                //Nächstes Element merken
        delete *platzalt;                        //Altes Element freigeben
        struct speicher *platzalt;                //Neuen Zeiger deklarieren
        platzalt=platzneu;                        //zum nächsten Element springen
}


z--;
}


std::cout << “Brennt er schon ?”;


return 0;


}