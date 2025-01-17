
#pragma once

#include <iostream>
#include <string>
using namespace std;

class Player1
{
	private:
		int hp;
		bool sword;
		bool shield;
		int potion; 
	
	public:
		Player1(){hp = 20; sword = false; shield = false; potion = 0; }
		
		void setHp(int s) {hp = hp + s; if (hp > 20){hp = 20;}};
		void setSword(bool s) {sword = s;};
		void setShield(bool s){shield = s;};
		void setPotion(int s){potion = potion + s;}; 
		
		int getHp(){return hp;};
		bool getSword(){return sword;};
		bool getShield(){return shield;};
		int getPotion(){return potion;};
		
		string showInventory(){
			string inventory = "";
			if (sword){inventory = inventory + "- 1 sword \n";}
			if (shield){inventory = inventory + "- 1 shield \n";}
			inventory = inventory + "- " + to_string(potion) + " potion(s) \n";
			return inventory;
			}
		
};
