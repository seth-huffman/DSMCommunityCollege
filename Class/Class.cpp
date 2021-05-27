/////////////////////////////////////////////////////
// Seth Huffman / 10/8/19  / sethwhuffman@gmail.com
/////////////////////////////////////////////////////

#include <iostream> 

using namespace std; 

class ParentClass {
    public:
        void Total(int Popcorn, int Candy, int Soda, int Ticket, int profit, string Movie);
        void Popcorn(int Popcorn);
        void Candy(int Candy);
        void Soda(int Soda);
        void Ticket(int Ticket, string Movie);
        void Profit(int Profit);
};

//////////////////////////////////


void ParentClass::Total(int Popcorn, int Candy, int Soda, int Ticket, int Profit, string Movie){
    ParentClass::Ticket(Ticket, Movie);
    cout << endl;
    
    ParentClass::Popcorn(Popcorn);
    ParentClass::Candy(Candy);
    ParentClass::Soda(Soda);
    ParentClass::Profit(Profit);
    cout << endl;
}

void ParentClass::Popcorn(int Popcorn) {
    cout << "Popcorn Left: " << Popcorn << endl;
}

void ParentClass::Candy(int Candy) {
    cout << "Candy Left: " << Candy << endl;
}

void ParentClass::Soda(int Soda) {
    cout << "Soda Left: " << Soda << endl;
}

void ParentClass::Profit(int Profit) {
    cout << "Total Profit: " << Profit << endl;
}

void ParentClass::Ticket(int Ticket, string Movie) {
    cout << Movie << " is showing and there are " << Ticket << "tickets left" << endl;
}

//////////////////////////////////

int main () 
{
    system("clear");

    ParentClass CinemaOne;
    ParentClass CinemaTwo;
    ParentClass CinemaThree;
    ParentClass CinemaFour;
    ParentClass CinemaFive;

    CinemaOne.Total(10, 20, 30, 40, 100, "The Godfather");
    CinemaTwo.Total(20, 30, 40 , 50, 76, "The Shawshank Redemption");
    CinemaThree.Total(30, 40, 50, 60, 34, "Schindler's List");
    CinemaFour.Total(40, 50, 60, 70, 67, "Raging Bull");
    CinemaFive.Total(50, 60, 70, 80, 24, "Casablanca");

  return 0; 
} 



//testing program = UML for each class that you make 
