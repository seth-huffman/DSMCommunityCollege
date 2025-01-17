////////////////////////////////////////
//  Seth Huffman Dec 1st 2019
////////////////////////////////////////


#include <iostream>
#include <vector>
#include <string>

using namespace std;

class HouseHunt
{
    public:
        void MovingAround(); 

    private:
        bool ItemOne; //Mail Key
        bool ItemTwo; //Skelton Key
        bool ItemThree; //Money
        bool ItemFour; //Batteries
        bool ItemFive; //Remote
        bool ItemSix; //Can Opener
        bool ItemSeven; //Food
        bool ItemEight; //Dog
        bool ItemNine; //Landlord key
        int PickRoom;
        int Counter;
};

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


void HouseHunt::MovingAround() {

    ItemOne = false;
    ItemTwo = false;
    ItemThree = false;
    ItemFour = false;
    ItemFive = false;
    ItemSix = false;
    ItemSeven = false;
    ItemEight = false;
    ItemNine = false;
    PickRoom = 0;
    Counter = 0;


    while(PickRoom <= 15 && Counter != 20){

        cout << "HALLWAY: Time to go checkout some of the other rooms." << endl << "Type a number 1 - 16 to enter that room: ";
        cin >> PickRoom;

        switch(PickRoom) {
            case 1: //Mail Key
                system ("clear");
                cout << "In this room you will find a key that unlocks the mailboxes in room 3." << endl << endl;
            break;
            case 2:
                cout << "Distraction room" << endl << endl;
            break;
            case 3: //Skelton Key
                system ("clear");
                cout << "In this room you will use a key to unlock the mailboxes to find a skelton key that will allow you now to get into all rooms but room 16." << endl << endl;
            break;
            case 4:
                cout << "Distraction room" << endl << endl;
            break;
            case 5: //Money
                system ("clear");
                cout << "In this room you will find money that will allow you to buy batteries in room 7." << endl << endl;
            break;
            case 6:
                system ("clear");
                cout << "Distraction room" << endl << endl;
            break;
            case 7: //Batteries
                system ("clear");
                cout << "In this room you will use money to buy batteries for a remote in room 9." << endl << endl;
            break;
            case 8:
                system ("clear");
                cout << "Distraction room" << endl << endl;
            break;
            case 9: //Remote
                system ("clear");
                cout << "In this room you will use use your batteries with a remote to change a TV station for someone and then you get to barrow the remote for room 11." << endl << endl;
            break;
            case 10:
                system ("clear");
                cout << "Distraction room" << endl << endl;
            break;
            case 11: //Can Opener
                system ("clear");
                cout << "In this room you will use the remote that you recently obtained to get a can opener for food that you will fint in room 13." << endl << endl;
            break;
            case 12:
                system ("clear");
                cout << "Distraction room" << endl << endl;
            break;
            case 13: //Food
                system ("clear");
                cout << "In this room you find dog food and you will use the can opener that you recently obtained to open the food for in room 15." << endl << endl;
            break;
            case 14:
                system ("clear");
                cout << "Distraction room" << endl << endl;
            break;
            case 15: //Dog
                system ("clear");
                cout << "In this room you will use the dog food that you recently opened to get the key around the dogs neck for room 16." << endl << endl;
            break;
            case 16: //Landlord key
                system ("clear");
                cout << "In this room you will use the key from the dog to get in and pay your rent. Resulting in you winning." << endl << endl;
            break;
        }
    }
}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

int main() {
    system ("clear");
    cout << "Discription of the game" << endl << endl;

    HouseHunt person;

    person.MovingAround();


   return 0;
};
