package EvenOccurances;

import Interviews.EvenOccurances.Solution;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;
import static org.junit.jupiter.api.Assertions.assertEquals;

class SolutionTest {

    private Solution solution = new Solution();

    @Test
    void testEmptyArray() {
        int[] nums = new int[]{};

        boolean expected = true;
        boolean actual = solution.evenOccurrences(nums);
        boolean actual2 = solution.evenOccurrences2(nums);
        boolean actual3 = solution.evenOccurrences3(nums);
        boolean actual4 = solution.evenOccurrences4(nums);

        assertEquals(expected, actual);
        assertEquals(expected, actual2);
        assertEquals(expected, actual3);
        assertEquals(expected, actual4);
    }

    @Test
    void testAllEvenOccurrences() {
        int[] nums = new int[]{2, 2, 4, 4};

        boolean expected = true;
        boolean actual = solution.evenOccurrences(nums);
        boolean actual2 = solution.evenOccurrences2(nums);
        boolean actual3 = solution.evenOccurrences3(nums);
        boolean actual4 = solution.evenOccurrences4(nums);

        assertEquals(expected, actual);
        assertEquals(expected, actual2);
        assertEquals(expected, actual3);
        assertEquals(expected, actual4);
    }

    @Test
    void testOneOddOccurrence() {
        int[] nums = new int[]{2, 2, 4, 4, 1};

        boolean expected = false;
        boolean actual = solution.evenOccurrences(nums);
        boolean actual2 = solution.evenOccurrences2(nums);
        boolean actual3 = solution.evenOccurrences3(nums);
        boolean actual4 = solution.evenOccurrences4(nums);

        assertEquals(expected, actual);
        assertEquals(expected, actual2);
        assertEquals(expected, actual3);
        assertEquals(expected, actual4);
    }

    @Test
    void testSingleNumber() {
        int[] nums = new int[]{1};

        boolean expected = false;
        boolean actual = solution.evenOccurrences(nums);
        boolean actual2 = solution.evenOccurrences2(nums);
        boolean actual3 = solution.evenOccurrences3(nums);
        boolean actual4 = solution.evenOccurrences4(nums);

        assertEquals(expected, actual);
        assertEquals(expected, actual2);
        assertEquals(expected, actual3);
        assertEquals(expected, actual4);
    }
}