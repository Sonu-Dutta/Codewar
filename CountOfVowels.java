//  Return the number (count) of vowels in the given string.
//  We will consider a, e, i, o, u as vowels for this Kata (but not y).
//  The input string will only consist of lower case letters and/or spaces.

public class  CountOfVowels{
    public static int getCount(String str) {
        // return str.replaceAll("(?i)[^aeiou]", "").length();
        int vowelsCount = 0; for(int i = 0; i < str.length(); i++) 
               {
                switch(str.charAt(i)) { 
                    case 'a': 
                    case 'e': 
                    case 'i': 
                    case 'o': 
                    case 'u':    
                    vowelsCount++; 
                } 
            } 
            return vowelsCount;
    }
    public static void main(String[] args) {
        System.out.println(getCount("sonu"));
    }
}
