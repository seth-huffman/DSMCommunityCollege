////////////////////////////////////////////////////////////
/// Seth Huffman - septemeber 15th - sethwhuffman@gmail.com
////////////////////////////////////////////////////////////
#include <iostream>
#include <fstream>
using namespace std;



int main()
{

    string A = "-  American League";
    string N = "-  National League";
    string NA = "-  No Winner";

        ofstream file;
        file.open ("outputbb.txt");

    file << "Anaheim Angels  " << N << endl;
    file << "Arizona Diamondbacks  " << A << endl;
    file << "Atlanta Braves  " << N << endl;
    file << "Baltimore Orioles  " << N << endl;
    file << "Boston Americans  " << N << endl;
    file << "Boston Braves  " << N << endl;
    file << "Boston Red Sox  " << N << endl;
    file << "Brooklyn Dodgers  " << N << endl;
    file << "Chicago Cubs  " << N << endl;
    file << "Chicago White Sox  " << N << endl;
    file << "Cincinnati Reds  " << N << endl;
    file << "Cleveland Indians  " << N << endl;
    file << "Detroit Tigers  " << N << endl;
    file << "Florida Marlins  " << N << endl;
    file << "Kansas City Royals  " << N << endl;
    file << "Los Angeles Dodgers  " << N << endl;
    file << "Milwaukee Braves  " << N << endl;
    file << "Minnesota Twins  " << N << endl;
    file << "New York Giants  " << N << endl;
    file << "New York Mets  " << N << endl;
    file << "New York Yankees  " << N << endl;
    file << "No Winner  " << N << endl;
    file << "Oakland Athletics  " << N << endl;
    file << "Philadelphia Athletics  " << N << endl;
    file << "Philadelphia Phillies  " << N << endl;
    file << "Pittsburgh Pirates  " << N << endl;
    file << "San Francisco Giants  " << N << endl;
    file << "St. Louis Cardinals  " << N << endl;
    file << "Toronto Blue Jays  " << N << endl;
    file << "Washington Senators  " << N << endl;

   file.close();
 return 0;

}
