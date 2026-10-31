class Solution {
    public boolean hasDuplicate(int[] nums) {
        
        HashSet<Integer> set = new HashSet<>();

        for ( int num : nums){
            set.add(num);
        }

        Boolean ans = (set.size() != nums.length) ? true: false;

        return ans;


    }
}