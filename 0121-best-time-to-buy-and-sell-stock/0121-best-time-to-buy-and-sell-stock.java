// class Solution {
//     public int maxProfit(int[] prices) {
//         int max = 0;
//         int profit = 0;
//         int j=1, i=0;
//         while(j<prices.length){
//                 if(prices[i]<prices[j]){
//                     profit = prices[j]-prices[i];
//                     max = max>profit?max:profit;
//                     j++;
//                 }
//                 else{
//                     i++;
//                     j=i+1;
//                 }
//         }
//     return max;
//     }
// }
class Solution {
    public int maxProfit(int[] prices) {
        int max_profit=0;
        int min_price=Integer.MAX_VALUE;

        for(int i=0;i<prices.length;i++){
            min_price=Math.min(min_price,prices[i]);
            max_profit=Math.max(max_profit,prices[i]-min_price);
        }
        return max_profit;
    }
}