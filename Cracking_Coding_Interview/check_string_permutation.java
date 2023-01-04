package Cracking_Coding_Interview;

public class check_string_permutation {
    public static boolean perm(String s, String t) {
        if (s.length() != t.length())
            return false;

        int letters[] = new int[128];
        char[] s_array = s.toCharArray();

        for (char i : s_array) {
            letters[i]++;
        }

        for (int j = 0; j < t.length(); j++) {
            int char_num = (int) t.charAt(j);
            letters[char_num]--;
            if (letters[char_num] < 0) {
                return false;
            }
        }

        return true;
    }

    public static void main(String[] args) {
        System.out.println(perm("aabc", "aafc"));
    }
}
