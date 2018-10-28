package LeetCode.UniqueEmailAddresses;

import java.util.HashSet;
import java.util.Set;

public class Solution {

    /*
     * Time: O(n)
     * Space: O(n)
     */

    public int numUniqueEmails(String[] emails) {
        Set<String> set = new HashSet<>();

        for (String email : emails) {
            String[] parts = email.split("@");
            String local = parseLocal(parts[0]);
            String domain = parts[1];

            set.add(local + '@' + domain);
        }

        return set.size();
    }

    private String parseLocal(String local) {
        StringBuilder sb = new StringBuilder();

        for (char c : local.toCharArray()) {
            if (c != '.') {
                if (c == '+') {
                    return sb.toString();
                }

                sb.append(c);
            }
        }

        return sb.toString();
    }
}
