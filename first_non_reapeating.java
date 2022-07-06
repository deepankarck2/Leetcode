import java.util.HashMap;

public class first_non_reapeating {
    public int firstNonRepeatingCharacter(String string) {
       HashMap<Character, Integer> dict= new HashMap<Character, Integer>();
        
        for(int i = 0; i< string.length(); i++){
            char chars = string.charAt(i);
            dict.putIfAbsent(chars, 0);
            dict.put(chars, dict.get(chars)+1);  

        }

        for(int i=0; i<string.length(); i++){
            char chars = string.charAt(i);
            if(dict.get(chars) == 1){
                return i; 
            }
        }
        return -1;
}
      
    public static void main(String[] args) {
        
        first_non_reapeating ans = new first_non_reapeating();
        System.out.println(ans.firstNonRepeatingCharacter("abcdcaf"));

    }

}
