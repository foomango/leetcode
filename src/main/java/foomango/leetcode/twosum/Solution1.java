package foomango.leetcode.twosum;

import java.util.Arrays;


public class Solution1 {

    public int[] towSum(int[] nums, int target) {
        int[] copyNums = nums.clone();
        
        Arrays.sort(copyNums);
        
        int i = 0;
        int j = copyNums.length - 1;
        while (i < j) {
            int sum = copyNums[i] + copyNums[j];
            if (sum < target) {
                i++;
            } else if (sum > target) {
                j--;
            } else {
                int[] answers = new int[2];
                int m = 0;
                int n = 0;
                
                for (m = 0; m < nums.length && n < answers.length; m++) {
                    if (nums[m] == copyNums[i] || nums[m] == copyNums[j]) {
                        answers[n++] = m + 1;
                    }
                }
                              
                return answers;
            }
        }
        
        return null;
    }
}
