package Interviews.EvenOccurances;

import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Set;

public class Solution {

    /*
     * Time: O(2*n)
     * We need to iterate through the entire array twice.
     * The first time we keep track of all the occurrences of a particular number
     * The second time we check that it has an even number of occurrences.
     *
     * Space: O(n)
     * We use a hash-map to keep track of all unique numbers in the array. There could be n unique numbers in the
     * array.
     */

    public boolean evenOccurrences(int[] nums) {

        if (nums == null || nums.length == 0) return true;

        HashMap<Integer, Integer> map = new HashMap<>();

        for (int n : nums) {
            map.put(n, map.getOrDefault(n, 0) + 1);
        }

        for (int n : nums) {
            if (n % 2 == 1) {
                return false;
            }
        }

        return true;
    }

    /*
     * Time: O(n)
     * We only need to iterate through the entire array once to find out if each element contains an even occurrence.
     * Since we are ONLY looking for even occurrences, if an element n is not already in the set, this is the first time
     * that we have seen it. This means there is currently an odd occurrence of that element.
     * If we come across an element and it is already in the set, we know that this is the second time that we have seen
     * it. We can remove it from the set.
     *
     * If the size of the set does not equal to zero, we know that there must be some odd occurrence of a number
     * in the array.
     *
     * Space: O(n)
     * We are using a set to keep track of all the unique numbers in the array. There could be n unique numbers in the
     * array that we need to store.
     */

    public boolean evenOccurrences2(int[] nums) {

        if (nums == null || nums.length == 0) return true;

        Set<Integer> set = new HashSet<>();

        for (int n : nums) {
            if (set.contains(n)) {
                set.remove(n);
            } else {
                set.add(n);
            }
        }

        return set.size() == 0;
    }

    /*
     * Time: O(n*log(n))
     *
     * Space: O(1)
     * Use the built in Java sort which uses quick-sort on the elements of the array.
     */

    public boolean evenOccurrences3(int[] nums) {

        if (nums == null || nums.length == 0) return true;

        Arrays.sort(nums);

        boolean isEven = false;

        for (int i = 0; i < nums.length - 1; i++) {
            if (nums[i] == nums[i + 1]) {
                isEven = !isEven;
            } else {
                if (isEven) {
                    isEven = !isEven;
                } else {
                    return isEven;
                }
            }
        }

        return isEven;
    }

    /*
     * Time: O(n*log(n))
     *
     * Space: O(1)
     * Use the built in Java sort which uses quick-sort on the elements of the array.
     */

    public boolean evenOccurrences4(int[] nums) {

        if (nums == null || nums.length == 0) return true;

        Arrays.sort(nums);

        int occurrences = 1;

        for (int i = 0; i < nums.length - 1; i++) {
            if (nums[i] == nums[i + 1]) {
                occurrences++;
            } else {
                if (occurrences % 2 == 0) {
                    occurrences = 1;
                } else {
                    return false;
                }
            }
        }

        return occurrences % 2 == 0;
    }
}
