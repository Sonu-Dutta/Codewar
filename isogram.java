
//  An isogram is a word that has no repeating letters, consecutive or non-consecutive. 
// Implement a function that determines whether a string that contains only letters is an isogram. 
// Assume the empty string is an isogram. Ignore letter case.
//  Example: (Input --> Output)
//  "Dermatoglyphics" --> true 
// "aba" --> false 
// "moOse" --> false (ignore letter case)
public class isogram {
    public static boolean isIsogram(String str) {
        return str.length() == str.toLowerCase().chars().distinct().count();
    }
    public static void main(String[] args) {
        System.out.println(isIsogram("Dutta"));
        System.out.println(isIsogram("Sonu"));
    }
}
