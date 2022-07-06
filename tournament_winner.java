import java.util.*; 

public class tournament_winner {

    public String tournamentWinner(ArrayList<ArrayList<String>> competitions, ArrayList<Integer> results) {
        HashMap<String,Integer> dict = new HashMap<String, Integer>(); 
        int row_count = 0; 

        for(int i: results){
            String team = ""; 
            if(i == 0 ){
                team = competitions.get(row_count).get(1); 
               
            }
            else{
                team = competitions.get(row_count).get(0);
            }
            dict.putIfAbsent(team, 0); 
            dict.put(team, dict.get(team)+3);

            row_count++; 
        }
        //Maybe look for other better approach
        //HOW TO GET MAX VALUE IN JAVA HASH_MAP?
        String maxKey = null; 
        for(String keys: dict.keySet()){
            if(maxKey == null || dict.get(maxKey) < dict.get(keys)){
                maxKey = keys;
            }
        }
        return maxKey; 
    }

 public static void main(String[] args) {
    
    ArrayList<ArrayList<String>> competitions = new ArrayList<ArrayList<String>>();
    ArrayList<String> competition1 = new ArrayList<String>(Arrays.asList("HTML", "C#"));
    ArrayList<String> competition2 = new ArrayList<String>(Arrays.asList("C#", "Python"));
    ArrayList<String> competition3 = new ArrayList<String>(Arrays.asList("Python", "HTML"));
    competitions.add(competition1);
    competitions.add(competition2);
    competitions.add(competition3);
    ArrayList<Integer> results = new ArrayList<Integer>(Arrays.asList(0, 0, 1));

    String ans = new tournament_winner().tournamentWinner(competitions, results);
    System.out.println(ans);
 }
}
