// CSE 110     : CSE110 / online
// Assignment  : Player.java
// Author      : Seth Huffman swhuffma
// Description : Creates player

class Player {
    private String name;
    private double attackStat, blockStat;

    public String getName() {
        return name;
    }

    public double getBlockStat() {
        return blockStat;
    }

    public double getAttackStat() { 
        return attackStat;
    }

    public void setAttackStat(double attackStat) {
        this.attackStat = attackStat;
    }

    public void setBlockStat(double blockStat) {
        this.blockStat = blockStat;
    }

    public void printPlayerInfo() {
        System.out.print("");
    }

}