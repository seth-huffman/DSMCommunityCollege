package module0;
import java.util.Scanner; 

/**
* This will ask the user for price of coffee and price of donut. 
* 
* The output will be the total of both the price of coffe and the price of the donut. Then add those together.
* @author Seth Huffman
* 
*/

public class PriceSet {
    public static void main(String[] args) throws Exception {

        Scanner userInput = new Scanner(System.in); 

        System.out.println("Price of Coffee");
        double PriceOfCoffee = userInput.nextDouble();

        System.out.println("Price of Donut");
        double PriceOfDonut = userInput.nextDouble();

        double PriceOfDonutAndCoffee = PriceOfCoffee + PriceOfDonut;

        System.out.printf("Total: " + PriceOfDonutAndCoffee + " (" + PriceOfCoffee + " + " + PriceOfDonut + ")" );
    }
}