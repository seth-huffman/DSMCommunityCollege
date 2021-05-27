/////////////////////////////////////////////////////
// Seth Huffman sethwhuffman@gmail.com 10/8/19
/////////////////////////////////////////////////////

#include <iostream>
#include <string>
#include <sstream>
#include <fstream>

using namespace std;

struct CreatingStructVariable {
  string UserVariable;
} StructConnection;


int main ()
{

  cout << "Enter a struct variable: ";
  getline (cin,StructConnection.UserVariable);

  cout << "Your struct variable: ";
  cout << StructConnection.UserVariable;

 ofstream myfile;
  myfile.open ("example.txt");
  myfile << StructConnection.UserVariable;
  myfile.close();

  return 0;
}

