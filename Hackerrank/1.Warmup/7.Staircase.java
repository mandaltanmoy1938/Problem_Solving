import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        
        StringBuilder stringBuilder=new StringBuilder();
        for (int i=0;i<n;i++){
            stringBuilder.append(" ");
        }
        for (int i=1; i<=n;i++){
            stringBuilder.setCharAt(n-i,'#');
            System.out.println(stringBuilder);
        }
    }
}