class Solution {
    public int maxProfit(int[] prices) {
        int max = 0;
        int profit = 0;
        int j=1, i=0;
        while(j<prices.length){
                if(prices[i]<prices[j]){
                    profit = prices[j]-prices[i];
                    max = max>profit?max:profit;
                    j++;
                }
                else{
                    i++;
                    j=i+1;
                }
        }
    return max;
    }
}