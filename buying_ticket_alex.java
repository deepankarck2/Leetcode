class Result {

    /*
     * Complete the 'waitingTime' function below.
     *
     * The function is expected to return a LONG_INTEGER.
     * The function accepts following parameters:
     *  1. INTEGER_ARRAY tickets
     *  2. INTEGER p
     */

    public static long waitingTime(List<Integer> tickets, int p) {
    // Write your code here
        int ticket_index = 0; 
        long count = 0; 
        int n = tickets.size(); 
        
        while( tickets.get(p) > 0 ){
             if(tickets.get(ticket_index) > 0 ){
                tickets.set(ticket_index, tickets.get(ticket_index)-1); 
                count++; 
             }

             ticket_index = (ticket_index + 1) % n ; 
        }
        
        return count; 
    }
    
}
