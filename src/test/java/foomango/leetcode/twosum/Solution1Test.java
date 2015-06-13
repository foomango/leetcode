package foomango.leetcode.twosum;

import static org.junit.Assert.*;

import org.junit.Test;

public class Solution1Test {

    protected static int[][] numbers = new int[][] {
        new int[]{0, 4, 3, 0},
        new int[]{-1, -2, -3, -4, -5}
        };
    protected static int[][] answers = new int[][] {
        new int[]{1, 4},
        new int[]{3, 5}};
    protected static int target[] = new int[] {0, -8};
    
    @Test
    public void testTwoSum() {
        Solution1 solution1 = new Solution1();
        for (int i = 0; i < target.length; i++) {
            assertArrayEquals(answers[i], solution1.towSum(numbers[i], target[i]));
        }
    }
}
