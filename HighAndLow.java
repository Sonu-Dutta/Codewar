// In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.
// Examples
// highAndLow("1 2 3 4 5") // return "5 1" 
// highAndLow("1 2 -3 4 5") // return "5 -3" 
// highAndLow("1 9 3 4 -5") // return "9 -5"

public class HighAndLow{
    public static String HighAndLow1(String numbers) {
        int max = Integer.MIN_VALUE;
        int min = Integer.MAX_VALUE;
        String nums[] = numbers.split(" ");
        for (String s : nums) {
            int num = Integer.parseInt(s);
            max = Math.max(max, num);
            min = Math.min(min, num);
        }
        return "" + max + " " + min;
    }
    
    public static void main(String[] args) {
        System.out.println(HighAndLow1("1 2 -3 4 5") );
    }
        
}
