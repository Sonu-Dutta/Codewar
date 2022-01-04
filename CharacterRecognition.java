//  Character recognition software is widely used to digitise printed texts. Thus the texts can be edited, searched and stored on a computer.
//  When documents (especially pretty old ones written with a typewriter), are digitised character recognition softwares often make mistakes.
//  Your task is correct the errors in the digitised text. You only have to handle the following mistakes:

//  S is misinterpreted as 5
//  O is misinterpreted as 0
//  I is misinterpreted as 1

public class CharacterRecognition {
    public static String correct(String string) {
        // return string.replace("5", "S").replace("0", "O").replace("1", "I");
        // return string.replaceAll("5","S") .replaceAll("0","O") .replaceAll("1","I");
        if(string ==null || string.isEmpty()) { 
            return string; 
        } 
        string = string.replace("1","I").replace("0","O").replace("5","S"); 
        return string;

    }
    public static void main(String[] args) {
        System.out.println(correct("50NU"));
    }
}
