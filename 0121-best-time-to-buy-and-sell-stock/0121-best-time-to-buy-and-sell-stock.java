class Solution {
    // public int rec(int i,boolean canBuy){
    //     if(i==prices.length){
    //         return 0;
    //     }
    //     if(canBuy){
    //         int pick = -prices[i]+rec(i+1);
    //         int notPick = rec(i+1)
    //     }
    //     else{
    //         int pick = prices[i]+rec(i+1)
    //         int 
    //     }
    // }
    public int maxProfit(int[] prices) {
        int min = Integer.MAX_VALUE;
        int maxprofit = 0;
        int cost = 0;
        for(int i=0; i<prices.length; i++){
            if(min>prices[i]) min = prices[i];
            cost = prices[i] - min;
            maxprofit = Math.max(cost, maxprofit);
        }
        return maxprofit;
    }
}