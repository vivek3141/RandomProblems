public class Problems{
    public static void writeSquares(int n){
        if(n == 1){
            System.out.print(Math.pow(n, 2) + ", ");

        }
        else if(n % 2 == 0){
            System.out.print(Math.pow(n, 2) + ", ");
            writeSquares(n + 2);
            //writeSquares(n - 2);
        }
        else if(n % 2 == 1){
            System.out.print(Math.pow(n, 2) + ", ");
            writeSquares(n - 2);
            //writeSquares(n - 1);
        }
        else{
            
        }
    }
    public static void main(String[] args){
        writeSquares(7);
    }
}