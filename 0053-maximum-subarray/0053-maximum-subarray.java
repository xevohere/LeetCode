class Solution {
    public int maxSubArray(int[] nums) {
        int max = 0; int sum = 0; int p=0;
        for(int i=0; i<nums.length; i++){
            sum = sum + nums[i];
            if(sum<0){
                sum=0;
            }
            if(sum>max)
                max=sum;
        }
        int count = 0;
        int maxi=-999999;
        for(int i=0; i<nums.length; i++){
            if(nums[i]<0){
                count++;
                if(nums[i]>maxi)
                    maxi=nums[i];
            }
        }
        if(count==nums.length){
            return maxi;
        }

    return max;
    }
}