/////////////////////////////////////////////////////
// Seth Huffman / 10/1/19  / sethwhuffman@gmail.com
/////////////////////////////////////////////////////

#include <iostream> 
using namespace std; 
  
int main () 
{ 
    int x = 2; 
    int *y = new(nothrow) int[x]; 
  
    for (int i = 0; i < x; i++) {
      y[i] = i+1; 

      for (int i = 0; i < x; i++) {
        cout << y[i] << " "; 
      }

    }
    delete[] y;
    
  return 0; 
} 
