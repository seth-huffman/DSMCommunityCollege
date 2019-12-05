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
                if (ItemOne == false) {
                    cout << "ROOM 1: You found a key!" << endl << endl;
                    ItemOne = true;
                } else {
                    cout << "ROOM 1: You always forget to make your bed. Oh, look a bird! (Leaving room)" << endl << endl;
                }

            break;
            case 2:
                if (ItemTwo == false) {
                    cout << "Jiggle Jiggled. Ohh... Locked out" << endl << endl;
                } else {
                    cout << "ROOM 2: It looks like your neighbor is building some sort of bomb. Get out fast." << endl << endl;
                }
            break;
            case 3: //Skelton Key
                system ("clear");
                if (ItemOne == true && ItemTwo == false) {
                    cout << "ROOM 3: You used the key you found to open the mailboxes and found a skelton key to open everyones rooms!" << endl << endl;
                    ItemTwo = true;
                } else if (ItemOne == true && ItemTwo == true) {
                    cout << "ROOM 3: Nothing to fun going on in here... Lets get out of here." << endl << endl;
                } else {
                    cout << "ROOM 3: The Mailroom is nice for holding mail." << endl << endl;
                }
            break;
            case 4:
                system ("clear");                
                if (ItemTwo == false) {
                    cout << "Jiggle Jiggled. Ohh... Locked out" << endl << endl;
                } else {
                    cout << "ROOM 4: Woof Buzz, it smells like someone forgot to flush. You need to get out before you get sick." << endl << endl;
                }
            break;
            case 5: //Money
                system ("clear");
                if (ItemTwo == false) {
                    cout << "Jiggle Jiggled. Ohh... Locked out" << endl << endl;
                } else if (ItemTwo == true && ItemThree == false) {
                    cout << "ROOM 5: After digging through the couch cushions you found some money." << endl << endl;
                    ItemThree = true;
                } else if (ItemTwo == true && ItemThree == true) {
                    cout << "ROOM 5: Man, no one seems to use this community room any more. Lets go find something more lively." << endl << endl;
                } else {
                    cout << "ROOM 5: Welcome to the community room. Doesn't seem to be much action in here..." << endl << endl;
                }
            break;
            case 6:
                system ("clear");
                if (ItemTwo == false) {
                    cout << "Jiggle Jiggled. Ohh... Locked out" << endl << endl;
                } else {
                    cout << "ROOM 6: I think you just caught grandma making out with Santa under the mistletoe. I shouldn't be here." << endl << endl;
                }
            break;
            case 7: //Batteries
                system ("clear");
                if (ItemTwo == false) {
                    cout << "Jiggle Jiggled. Ohh... Locked out" << endl << endl;
                } else if (ItemThree == true && ItemFour == false) {
                    cout << "ROOM 7: You use your money that you found to get some fresh batteries from Ned. " << endl << endl;
                    ItemFour = true;
                } else if (ItemThree == true && ItemFour == true) {
                    cout << "ROOM 7: Ned looks to be gaming away again" << endl << endl;
                } else {
                    cout << "ROOM 7: Ned has made his room into a gamers paradice and it appears that he is selling some stuff but you have no money..." << endl << endl;
                }
            break;
            case 8:
                system ("clear");
                if (ItemTwo == false) {
                    cout << "Jiggle Jiggled. Ohh... Locked out" << endl << endl;
                } else {
                    cout << "ROOM 8: This place looks like it is infested with mice... Gross! I'm out." << endl << endl;
                }
            break;
            case 9: //Remote
                system ("clear");
                if (ItemTwo == false) {
                    cout << "Jiggle Jiggled. Ohh... Locked out" << endl << endl;
                } else if (ItemFour == true && ItemFive == false) {
                    cout << "ROOM 9: You use your batteries to change Edna's TV station so she will let you take her remote." << endl << endl;
                    ItemFive = true;
                } else if(ItemFour == true && ItemFive == true) {
                    cout << "ROOM 9: Looks like Edna is already asleep. So much for watching TV" << endl << endl;
                } else {
                    cout << "ROOM 9: You hear Edna Yelling at her TV saying the darn thing is broken." << endl << endl;
                }
            break;
            case 10:
                system ("clear");
                if (ItemTwo == false) {
                    cout << "Jiggle Jiggled. Ohh... Locked out" << endl << endl;
                } else {
                    cout << "ROOM 10: Is water leaking all over this this place or is this guy trying to build an indoor swimming pool? I'm gonna need some swimming trunks if I want be in here." << endl << endl;
                }
            break;
            case 11: //Can Opener
                system ("clear");
                if (ItemTwo == false) {
                    cout << "Jiggle Jiggled. Ohh... Locked out" << endl << endl;
                } else if (ItemFive == true && ItemSix == false) {
                    cout << "ROOM 11: You trade the chef a remote for a can opener. So he can use the TV remote." << endl << endl;
                    ItemSix = true;
                } else if(ItemFive == true && ItemSix == true) {
                    cout << "ROOM 11: Nothing better than a happy chef cooking and watching the cooking network." << endl << endl;
                } else {
                    cout << "ROOM 11: Duck! The chef is ticked off because he can't find his remote to watch the cooking network." << endl << endl;
                }
            break;
            case 12:
                system ("clear");
                if (ItemTwo == false) {
                    cout << "Jiggle Jiggled. Ohh... Locked out" << endl << endl;
                } else {
                    cout << "ROOM 12: TALK! TALK! TALK! It looks like you stumbled upon the apartment complexs gossip room. This isn't where you wanna be." << endl << endl;
                }
            break;
            case 13: //Food
                system ("clear");
                if (ItemTwo == false) {
                    cout << "Jiggle Jiggled. Ohh... Locked out" << endl << endl;
                } else if (ItemSix == true && ItemSeven == false) {
                    cout << "ROOM 13: You use the can opener to open a can of dog food. " << endl << endl;
                    ItemSeven = true;
                } else if (ItemSix == true && ItemSeven == true) {
                    cout << "ROOM 13: Whoa! Looks like you weren't the only one that decided to raid the food today." << endl << endl;
                } else {
                    cout << "ROOM 13: Appears to be a storage room for all of the Chefs food" << endl << endl;
                }
            break;
            case 14:
                system ("clear");
                if (ItemTwo == false) {
                    cout << "Jiggle Jiggled. Ohh... Locked out" << endl << endl;
                } else {
                    cout << "ROOM 14: ZZZZZ! Big Bob is passed out. Better not wake the big boy. Time to leave." << endl << endl;
                }
            break;
            case 15: //Dog
                system ("clear");
                if (ItemTwo == false) {
                    cout << "Jiggle Jiggled. Ohh... Locked out" << endl << endl;
                } else if (ItemSeven == true && ItemEight == false) {
                    cout << "ROOM 15: You slide the can of dog food over to buster. Looks like the little guy was just hungry. When he comes up to you see a key on his leash. So you take it. " << endl << endl;
                    ItemEight = true;
                } else if (ItemSeven == true && ItemEight == true) {
                    cout << "ROOM 15: Buster seems to want to be your best friend now." << endl << endl;
                } else {
                    cout << "ROOM 15: WOOF WOOF! Nice dog, nice dog. (RUN)" << endl << endl;
                }
            break;
            case 16: //Landlord key
                system ("clear");
                if (ItemTwo == false) {
                    cout << "Jiggle Jiggled. Ohh... Locked out" << endl << endl;
                } else if (ItemEight == true && ItemNine == false) {
                    cout << "ROOM 16: You're in! Place the check inside the room! Now you have a place to stay for another month. " << endl << endl;
                    ItemNine = true;
                } else {
                    cout << "ROOM 16: You really thought it was gonna be that easy to get into the landlords room?" << endl << endl;
                }
            break;
        }
    }
    
    if (ItemNine == true) {
        cout << "Congrats, you won!" << endl << endl;
    } else {
        cout << "OH NO! YOU GOT CAUGHT... Try again." << endl << endl;
    }
    
}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

int main() {
    system ("clear");
    cout << "Oh no, your rent is late again! If your landlord realizes that you didn't pay on time again you are gonna be kicked out for sure. Luckily you overheard from one of your neighbors that the landlord hasn't looked over the submitted rent checks for this month yet. Try to get your check in before the landlord comes back for the day. His room is on the top floors (room 18)." << endl << endl;

    HouseHunt person;

    person.MovingAround();


   return 0;
};
