//  Replace all vowel to exclamation mark in the sentence. aeiouAEIOU is vowel.

//  Examples
//  replace("Hi!") === "H!!"
//  replace("!Hi! Hi!") === "!H!! H!!"
//  replace("aeiou") === "!!!!!"
//  replace("ABCDE") === "!BCD!"
public class ReplaceByExclamationMark {
        public static String replace(final String s) {
            return s.replaceAll("[aeiouAEIOU]", "!");
    }
    public static void main(String[] args) {
        System.out.println(replace("hello sonu"));
    }
}
