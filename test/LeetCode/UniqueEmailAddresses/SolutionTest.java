package LeetCode.UniqueEmailAddresses;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class SolutionTest {

    private Solution solution = new Solution();

    @Test
    void testTwoUniqueEmails() {
        String[] emails = new String[]{"test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"};

        int expected = 2;
        int actual = solution.numUniqueEmails(emails);

        assertEquals(expected, actual);
    }
}