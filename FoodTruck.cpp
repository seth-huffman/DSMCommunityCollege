////////////////////////////////////////////////////////////////////////////////////////////
// Seth Huffman September 6th 2019 sethwhuffman@gmail.com
////////////////////////////////////////////////////////////////////////////////////////////

#include <iostream>
using namespace std;

int main(void)
{
    system("clear");

    //Inventory
    int HambugersStock = 0;
    int HotDogsStock = 0;
    int HambugersBunsStock = 0;
    int HotDogBunsStock = 0;
    int ChiliStock = 0;
    int FriesStock = 0;
    int SodaStock = 0;

    //Prices
    int price; 
    double SalesTax = 0.05;
    double SalesTaxTotal;
    double Total;

    //Order
    string product;
    int NewOrder;

    //Low Inventory
    string HamburgerLowInventory;
    string HamburgerBunLowInventory;
    string HotDogLowInventory;
    string HotDogBunLowInventory;
    string ChiliLowInventory;
    string ChiliDogLowInventory;
    string ChiliBurgerLowInventory;
    string ChiliFriesLowInventory;
    string FriesLowInventory;
    string SodaLowInventory;

    //Menu Items
    string MenuHamburger = "A - Hambugers = $5";
    string MenuHotDog = "B - Hot Dogs = $5";
    string MenuChili = "C - Chili (12oz) = $4";
    string MenuChiliBurger = "D - Chili on Burger (4oz) = $2";
    string MenuChiliDog = "E - Chili on Hot Dog (4oz) = $2 ";
    string MenuChiliFries = "F - Chili on Fries (4oz) = $2";
    string MenuFries = "G - Baskets of Fries = $7";
    string MenuSoda = "H - Can of Soda = $2";

    //User inputs inventory
    cout << "Please enter inventory for items." << endl;
    cout << endl << "Hambugers: ";
    cin >> HambugersStock;
    cout << "Hot Dogs: ";
    cin >> HotDogsStock;
    cout << "Hambugers Buns: ";
    cin >> HambugersBunsStock;
    cout << "Hot Dog Buns: ";
    cin >> HotDogBunsStock;
    cout << "Ounces of Chili: ";
    cin >> ChiliStock;
    cout << "Baskets of Fries: ";
    cin >> FriesStock;
    cout << "Cans of Soda: ";
    cin >> SodaStock;

    system("clear");

    //Loops for new order
    do {
        
        // Menu
        cout << MenuHamburger << HamburgerLowInventory << endl;
        cout << MenuHotDog << HotDogLowInventory << endl;
        cout << MenuChili << ChiliLowInventory << endl;
        cout << MenuChiliBurger << ChiliBurgerLowInventory << endl;
        cout << MenuChiliDog << ChiliDogLowInventory << endl;
        cout << MenuChiliFries << ChiliFriesLowInventory << endl;
        cout << MenuFries << FriesLowInventory << endl;
        cout << MenuSoda << SodaLowInventory << endl;

        int sum = 0;

        cout << endl << endl << "Please enter  menu a number or type 0 to exit: " << endl;

        //Entering order. Adds Price to Entered Item. Removes Items from Inventory.
        do {
            cout << endl << "Item's letter: ";
            cin >> product;
            if (product == "A" || product == "a") {
                price = 5; //Hamburger Price
                --HambugersStock;
                --HambugersBunsStock;
                if (HambugersStock <= 40 || HambugersBunsStock <= 15) {
                    HamburgerLowInventory = " (Inventory is Low)";
                }
            }
            if (product == "B" || product == "b") {
                price = 5; //Hotdog Price
                --HotDogsStock;
                --HotDogBunsStock;
                if (HotDogsStock <= 40 || HotDogBunsStock <= 15) {
                    HotDogLowInventory = " (Inventory is Low)";
                }
            }
            if (product == "C" || product == "c") {
                price = 4; //Chili Price
                --ChiliStock;
                if (ChiliStock <= 100) {
                    ChiliLowInventory = " (Inventory is Low)";
                }
            }
            if (product == "D" || product == "d") {
                price = 7; //Fries Price
                --FriesStock;
                if (FriesStock <= 15) {
                    FriesLowInventory = " (Inventory is Low)";
                }
            }
            if (product == "E" || product == "e") {
                price = 2; //Chili Burger Price
                --ChiliStock;
                --HambugersStock;
                --HambugersBunsStock;
                if (ChiliStock <= 100 || HambugersStock <= 40 || HambugersBunsStock <= 15) {
                    ChiliLowInventory = " (Inventory is Low)";
                }
            }
            if (product == "F" || product == "f") {
                price = 2; //Chili Dog Price
                --ChiliStock;
                --HotDogsStock;
                --HotDogBunsStock;
                if (ChiliStock <= 100 || HotDogsStock <= 40 || HotDogBunsStock <= 15) {
                    ChiliLowInventory = " (Inventory is Low)";
                }
            }
            if (product == "G" || product == "g") {
                price = 2; //Chili Fries Price
                --ChiliStock;
                --FriesStock;
                if (ChiliStock <= 100 || FriesStock <= 15) {
                    ChiliFriesLowInventory = " (Inventory is Low)";
                }
            }
            if (product == "H" || product == "h") {
                price = 2; //Soda Price
                --SodaStock;
                if (SodaStock <= 40) {
                    SodaLowInventory = " (Inventory is Low)";
                }
            }

            sum += price;
        } while ( product != "Z" );

        SalesTaxTotal = SalesTax * sum;
        Total = SalesTaxTotal + sum;

        cout << endl << "Total amount due =  $" << Total << endl << endl;

        cout << endl << "Start a new order? 0 for no, 1 for yes" << endl << endl;
        cin >> NewOrder;

    } while ( NewOrder >= 1 );
    return 0;
}




