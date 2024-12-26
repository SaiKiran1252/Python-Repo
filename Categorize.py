import java.util.*;

public class Categorize {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
         float height = scanner.nextFloat();
         if(height<150){
            System.out.println("Person is Dwarf.");
         }
         else if(height > 150 && height <= 165){
            System.out.println("Person is average heighted.");
         }
         else if(height > 165 && height <= 195){
            System.out.println("Person is taller.");
         }
         else{
            System.out.println("Abnormal height.");
         }

        scanner.close();
    }
}