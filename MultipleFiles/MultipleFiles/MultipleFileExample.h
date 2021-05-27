/////////////////////////////////////////////////////
// Seth Huffman / 10/8/19  / sethwhuffman@gmail.com
/////////////////////////////////////////////////////

#include <fstream>
#include <cstdlib>
#include <ctime>
#include <iomanip>
#include <iostream> 

using namespace std; 

#pragma once


class HTMLOptions {
  public:
    void OpenHTML(myfile);
    void TagOptionSelection(TagOption, variable, myfile);
};


// Vectors
// Array                   (string cars[4] = {"Volvo", "BMW", "Ford", "Mazda"};     cout << cars[0];)
// Operations                       (x+x;)
// Overloads
// Exceptions                       (Try, Throw, Catch)
// Pointing to Data Structures
// Objects