package Cracking_Coding_Interview;

public class URLify {
    public static void main(String[] args) {
        String in = "Mr John Smith    ";
        char[] input = in.toCharArray();
        int length = 13;
        int real_length = input.length - 1;

        for (int i = length - 1; i >= 0; i--) {
            if (input[i] != ' ') {
                input[real_length] = input[i];
                real_length--;
            } else if (input[i] == ' ') {
                input[real_length] = '0';
                input[real_length - 1] = '2';
                input[real_length - 2] = '%';
                real_length = real_length - 3;
            }
        }
        System.out.println(input);
    }
}
