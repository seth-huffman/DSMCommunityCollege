/////////////////////////////////////////////////////
// Seth Huffman / 10/8/19  / sethwhuffman@gmail.com
/////////////////////////////////////////////////////

#include <fstream>
#include <cstdlib>
#include <ctime>
#include <iomanip>
#include <iostream> 

#include "MultipleFileExample.h"

using namespace std; 

string variable;
int TagOption;

void OpenHTML(ofstream &myfile) {
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