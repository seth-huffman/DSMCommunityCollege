#include <iostream>
using namespace std;



int main()
{
    system("clear");

    int answer;
    int lives = 5;



    cout << "After turning a corner you see a hall way, empty and lined with bricks. You could swear it goes on for miles. BOOM! You start to hear a clicking noise that repeats over and over again. As if a gear was connected to a chain. Next you notice that one wall is slowly coming down in front of you and one behind you. Making it so that you will be trapped. You know if you if sprint now you might make it but you will be trapped inside. All of the sudden you see a shovel next to some grease. What do you do?";



    //Questions
    cout << endl;
    cout << endl << endl << "1) You are scared you wont make it in time so you pick up the grease. Throw it on the floor. Step back to get a running start. Then slide your entire way to the door." << endl;
    cout << endl << "2) Once you get to the closing wall you grab the shovel and wedge it so the wall will never close and you will be able to get back out if you want." << endl;
    cout << endl << "3) After seeing the bricks lining the walls you grab multiple bricks. Stacking them under the closing wall. Making sure it will never close." << endl;
    
    cout << endl << "Insert number: ";
    cin >> answer;
    
    system("clear");

    //Answers
    if (answer == 1) {
        cout << endl << "You got to scared and waited to long. By the time you put the grease down it was to late. You slid to slow braking your leg by the closing door but at least you got though" << endl;
    } else if (answer == 2) {
        cout << endl << "Perfect! The shovel worked like a charm and you have a way out. Great qick thinking." << endl;
    } else if (answer == 3) {
        cout << endl << "One of the bricks you picked up lead to a hole with a nest of snakes in it. One of the snakes sees you as threat and bites you on the leg. The door closes behind you and you barely make it through" << endl;
    } 


    if (answer == 1 || answer == 3) {
        --lives;
        cout << endl << endl << lives << endl;
    } 

    if (lives == 0) {
        cout << endl << endl << "Ganes Over" << endl;
    } 


    // cout << "You are now to weak to go on...Better luck next time";
}
