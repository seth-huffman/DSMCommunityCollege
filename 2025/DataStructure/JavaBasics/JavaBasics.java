// donut shop that sells coffee and donuts.
// set the prices of coffee and donuts. 

// prompts the user for the price of the coffee, 
// then the prices of a donut. 
// In one line, use a printf() to output to the user the two prices.

// Name your package module0
// Include a Javadoc style comment with short program description and @author
// Name your class PriceSet
// The file will be PriceSet.java
// Recall in Java the file and class name are identical or a syntax error is generated
// Use appropriate data types 
//  Java built-in numeric types: int, long, short, double, float
// Prompt the user on I/O
// Handle exceptions
// Select one of the methods provided
// Follow the format and comment style given in Java Input
// Use printf() to format output as show in Java Output
// Review the rubric for point break down to ensure you attempt all the points 

// import java.util.Scanner;


import java.util.Scanner; // import the Scanner class 

class Main {
  public static void main(String[] args) {
    Scanner myObj = new Scanner(System.in);
    String userName;
    
    // Enter username and press Enter
    System.out.println("Enter username"); 
    userName = myObj.nextLine();   
       
    System.out.println("Username is: " + userName);        
  }
}

              