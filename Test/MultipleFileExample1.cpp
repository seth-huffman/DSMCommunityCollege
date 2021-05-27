/////////////////////////////////////////////////////
//Seth Huffman / 10/8/19  / sethwhuffman@gmail.com
/////////////////////////////////////////////////////

#include <fstream>
#include <cstdlib>
#include <ctime>
#include <iomanip>
#include <iostream> 
#include <vector> 

using namespace std; 

//class & Objects
class HTMLOptions {
  public:
    void OverloadFunctions(ofstream &myfile);
    void OverloadFunctions(int TagOption, string variable, ofstream &myfile);
};

//////////////////////////////////////////

string variable;
int TagOption;

//OverloadFunctions
void OverloadFunctions(ofstream &myfile) {
    myfile << "<!doctype html> \n ";
    myfile << "<html class=\"no-js\" lang=\"en\"> \n ";
    myfile << "<head> \n ";
    myfile << "<meta charset=\"utf-8\"> \n ";
    myfile << "<title>Tester HTML Doc</title> \n ";
    myfile << "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\"> \n ";
    myfile << "<link rel=\"manifest\" href=\"site.webmanifest\"> \n ";
    myfile << "<link rel=\"stylesheet\" href=\"style.css\"> \n ";
    myfile << "<meta name=\"theme-color\" content=\"#fafafa\"> \n ";
    myfile << "</head> \n ";
    myfile << "<body> \n ";
}

//OverloadFunctions
void OverloadFunctions(int TagOption, string variable, ofstream &myfile) {
    do {
        cout << "\nPlease Type Required Tag Option:";
        cin >> TagOption;

        if (TagOption < 8) {
            cout << "Please Type One Word Variable:";
            cin >> variable;
        };
        
        switch (TagOption) 
        {
            case 1:
                myfile << "<h1>";
                myfile << variable;
                myfile << "</h1> \n ";
            break;
            case 2:
                myfile << "<h2>";
                myfile << variable;
                myfile << "</h2> \n ";
            break;
            case 3:
                myfile << "<h3>";
                myfile << variable;
                myfile << "</h3> \n ";
            break;
            case 4:
                myfile << "<h4>";
                myfile << variable;
                myfile << "</h4> \n ";
            break;
            case 5:
                myfile << "<h5>";
                myfile << variable;
                myfile << "</h5> \n ";
            break;
            case 6:
                myfile << "<h6>";
                myfile << variable;
                myfile << "</h6> \n ";
            break;
            case 7:
                myfile << "<p>";
                myfile << variable;
                myfile << "</p> \n ";
            break;
            default:
                myfile << "</body> \n ";
                myfile << "</html> \n ";
            break;
        }
    } while(TagOption < 8);
    
}

//////////////////////////////////////////

//Data Structure
int main () 
{
    HTMLOptions PrintOutput;
    vector<int> vector;

    //Array
    string Array [] = { "Header", "Paragraph", "End Program" }; 

    //Operations
    //Vector
    for (int i = 1; i <= 8; i++) 
        vector.push_back(i); 

    system("clear");
    cout << "Tag Options \n \n";
    cout << Array[0] << " 1: " << vector.at(0) << endl;
    cout << Array[0] << " 2: " << vector.at(1) << endl;
    cout << Array[0] << " 3: " << vector.at(2) << endl;
    cout << Array[0] << " 4: " << vector.at(3) << endl;
    cout << Array[0] << " 5: " << vector.at(4) << endl;
    cout << Array[0] << " 6: " << vector.at(5) << endl;
    cout << Array[1] << " : " << vector.at(6) << endl;
    cout << Array[2] << " : " << vector.at(7) << endl;

    //Read/Write files
    //Adv. File I/O
    ofstream myfile;
    myfile.open ("example.html");
    OverloadFunctions(myfile);
    OverloadFunctions(TagOption, variable, myfile);
    myfile.close();

  return 0; 
} 