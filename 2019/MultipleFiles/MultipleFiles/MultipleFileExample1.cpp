/////////////////////////////////////////////////////
// Seth Huffman / 10/8/19  / sethwhuffman@gmail.com
/////////////////////////////////////////////////////

#include "MultipleFileExample.h"

#include <fstream>
#include <cstdlib>
#include <ctime>
#include <iomanip>
#include <iostream> 

using namespace std; 

int main () 
{
    HTMLOptions PrintOutput;

    system("clear");
    cout << "Tag Options \n \n";
    cout << "Header 1: 1 \n";
    cout << "Header 2: 2 \n";
    cout << "Header 3: 3 \n";
    cout << "Header 4: 4 \n";
    cout << "Header 5: 5 \n";
    cout << "Header 6: 6 \n";
    cout << "Paragraph: 7 \n";
    cout << "End Program: 8 \n";

    //Read/Write files
    //Adv. File I/O
    ofstream myfile;
    myfile.open ("example.html");
    PrintOutput.OpenHTML(myfile);
    PrintOutput.TagOptionSelection(TagOption, variable, myfile);
    myfile.close();

  return 0; 
} 