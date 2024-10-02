class Solution {
    public void sortColors(int[] nums) {
        int n = nums.length;
        int zero=0, one=0, two=0;
        for(int i=0; i<n; i++){
            if(nums[i]==0){
                zero++;
                continue;
            }
            if(nums[i]==1){
                one++;
                continue;
            }
            if(nums[i]==2){
                two++;
                continue;
            }
        }
        for(int i=0; i<n; i++){
            if(i<zero){
                nums[i]=0;
            }
            else if(i<(zero+one)){
                nums[i]=1;
            }
            else{
                nums[i]=2;
            }
        }   
    }
}