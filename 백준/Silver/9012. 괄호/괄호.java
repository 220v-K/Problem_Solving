import java.util.Scanner;
import java.util.Stack;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        Integer n = sc.nextInt();
        sc.nextLine();
        for (int i = 0; i < n; i++) {
            String input = sc.nextLine();

            Stack<Character> stack = new Stack<>();
            boolean flag = true;

            for (int j = 0; j < input.length(); j++) {
                char c = input.charAt(j);

                if (c == '(') {
                    stack.push(c);
                } else if (c == ')') {
                    if (!stack.isEmpty() && stack.peek() == '(') {
                        stack.pop();
                    } else {
                        System.out.println("NO");
                        flag = false;
                        break;
                    }
                }
            }

            if (!stack.isEmpty()) {
                System.out.println("NO");
                flag = false;
            }

            if (flag) {
                System.out.println("YES");
            }
        }
    }
}
