#include <iostream>
#include <string>
#include "characterClass.h" 
#include "room3.h"


using namespace std;


int main()
{
	Player1 character;
	if(room1Function(character)){
		cout << "Game complete!";
		cin.ignore(); 
	}
	
return 0;
}

