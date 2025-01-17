// Name your package module0
// Include a Javadoc style comment with short program description and @author

// Recall in Java the file and class name are identical or a syntax error is generated

// Java built-in numeric types: int, long, short, double, float
// Prompt the user on I/O
// Handle exceptions
// Select one of the methods provided
// Follow the format and comment style given in Java Input
// Use printf() to format output as show in Java Output
// Review the rubric for point break down to ensure you attempt all the points



import java.util.Scanner;  // Import the Scanner class

class PriceSet {
  public static void main(String[] args) {
    Scanner userInput = new Scanner(System.in);  // Create a Scanner object

    System.out.println("Price of Coffee");
    double PriceOfCoffee = userInput.nextDouble(); 

    System.out.println("Price of Donut");
    double PriceOfDonut = userInput.nextDouble(); 

    double PriceOfCoffeeAndDonut = PriceOfDonut + PriceOfCoffee;

    System.out.printf("Total: (" + PriceOfDonut + " + " + PriceOfCoffee + ") " + PriceOfCoffeeAndDonut);  // Output user input
  }
}