
public class GrassHopper { 
    public static int summation(int n) { 
        int sum = 0; 
        for (; n > 0; n--) { 
            sum += n; 
        } 
            return sum; 
        } 
        public static void main(String[] args) {
            System.out.println(summation(4));
            System.out.println(summation(10));
        }
    }
