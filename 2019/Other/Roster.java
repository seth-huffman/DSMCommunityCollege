// CSE 110     : CSE110 / online
// Assignment  : Roster.java
// Author      : Seth Huffman swhuffma
// Description : Creates roster

class Roster {
    private String name;
    private int[] players; 
    private int count; 
    private double attackStat, blockStat; 

    public Roster() {
    }
    
//     The addPlayer method should instantiate a new Player object with the name and stats provided in the argument values, and then add this Player to the roster's ArrayList<Player> object.
//     The default constructor should instantiate a new ArrayList object, and store a reference to this object in the Roster's players instance variable.
//     The overloaded constructor should instantiate a new ArrayList object, and store a reference to this object in the Roster's players instance variable. 
//     It should then open the open the roster file named in the parameter variable. 
//     It should then read in the data from this roster file and, for each line in the file, it should create a new Player object with the player name and stat data on that line, and add this Player to the ArrayList players.   
public void addPlayer(String name, double attackStat, double blockStat) {
        this.name = name;
        this.attackStat = attackStat;
        this.blockStat = blockStat;
    }

    public double getAttackStat() {
        return attackStat;
    }

    public double getBlockStat() {
        return blockStat;
    }
    
    public void setAttackStat(double attackStat) {
        this.attackStat = attackStat;
    }

    public void setBlockStat(double blockStat) {
        this.blockStat = blockStat;
    }
    //     The printPlayerInfo method should print out to the console, the name and stats for this player object. 
    //     The printout should look like this: Rachael Adams (attack = 3.36, block = 1.93)


    //     return the number of players currently stored in the roster's ArrayList<Player> object.
    public int countPlayers() {
        return count;
    }

    //     iterate through the roster's ArrayList<Player> object and 
    //     call the printPlayerInfo method on each of these Player objects. 
    public void printAllPlayers() {
        System.out.print("");
    }

    //     determine the two Player objects with the best attack stats (in descending order). 
    //     It should then call the printPlayerInfo method on these Player objects.
    public void printTopAttackers() {
        System.out.print("");
    }

    //     determine the two Player objects with the best block stats (in descending order).
    //     It should then call the printPlayerInfo method on these Player objects.
    public void printTopBlockers() {
        System.out.print("");
    }

    public String getName(String name) {
        return name;
    }

//     The getPlayerByName method should iterate through the roster's ArrayList<Player> object and search for a player with a name that is equal to the argument value. 
//     If such a Player is found, then this method should return a reference to that
//     Player object, otherwise this method should return null.
}






























//     The volleyball coach at Verde Valley High School would like some help managing her team. 
//     She would like a program to help her identify the best players. 
//     She has team rosters stored in text files that contain the names of her players (first name, then last name separated by a space), and their stats as attacks per set (a double) followed by blocks per set (a double). 
//     Higher stats are better. 
//     Each data field is separated by a space. 
//     For example, one line in a roster file would look like:
//     Gabrielle Reece 4.57 1.79
//     The coach would like the program to do the following:
//     Present a menu with the following options:
//     1. Open a roster file
//     2. List all players
//     3. List top attackers
//     4. List top blockers
//     5. Add a player
//     6. Change a player's stats
//     7. Count players
//     8. Quit program

    // When the user chooses 1 to open a roster file, then the program will ask for the filename of a roster file, then open and read the data from that file into an ArrayList.
    // When the user chooses 2 to list all players, then the program will list the names and stats of all player players. 
    // When the user chooses 3 to list top attackers, then the program will determine and list the names and stats of the players with the top 2 attack stats.
    // When the user chooses 4 to list top blockers, then the program will determine and list the names and stats of the players with the top 2 stats for blocks.
    // When the user chooses 5 to add a player, then the program will prompt the user to enter the new player's name (first and last), attack stat (double), and block stat (double). 
    // The program should collect this information from the user, and then instantiate a new Player object with the given name and stats, and add that Player to the roster.
    // When the user chooses 6 to change a player's stats, then the program will prompt the user to enter the player's name (first and last). 
    // If there is a player on the roster with the given name, then the program will collect the new attack stat (double), and block stat (double), and will update the stat values for this player.
    // When the user chooses 7 to count players, then the program will display the number of players on the current roster.
    // When the user chooses 8 the program will end.
    // The main class has already been designed and written for this program (given in Assignment08.java). 
    // Carefully review the code in the Assignment08.java file and be sure that you understand how it works.
    // Your task is to implement the Player and Roster classes. 
    // The Player class will allow us to instantiate Player objects that will store the important information (name, attack stat, block stat) for a player. 
    // The Roster class will allow us to create and manage a roster of players - we will use an ArrayList<Player> to store the Player objects.






