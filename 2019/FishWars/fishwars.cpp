#include <random>
#include <iostream>
using std::cout; using std::endl;

//delete this function
std::vector<int> Deck()
{
    std::vector<int> deck;
    for(int i = 1; i <= 13; i++)
    {
        deck.push_back(i);
    }
    return deck;
}

int CPUTurn(std::vector<int> cpuDeck)
{
    //get a random number between 0 and deck_size - 1 then remove and return that one
    return cpuDeck.pop_back();
}
	
int compareCards(int userCard, int cpuCard, int userBattlePoints, int cpuBattlePoints)
{
    //do your thing
}

int main()
{
    //myvector.erase (myvector.begin() + i);
    //don't make random decks anymore, delete
    // in turn() get a random number 
    // or don't waste one of your functions on a deck, just copy that code here
    std::vector<int> userDeck;
    std::vector<int> cpuDeck;
    for(int i = 1; i <= 13; i++)
    {
        userDeck.push_back(i);
        cpuDeck.push_back(i);
    }

    int userBattlePoints = 0;
    int cpuBattlePoints = 0;
    int userpoints
    for(int i = 0; i < 13; i++)
    {
        //play here
    }
}

