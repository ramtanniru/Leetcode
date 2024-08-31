class Solution {
    public int maxProfit(int[] prices) {
        int [][][] dp = new int[prices.length][2][3];
        for(int i=0; i<prices.length; i++){
            for(int j=0; j<2; j++) {
                for(int k=0; k<3; k++) {
                    dp[i][j][k] = -1;
                }
            }
        }
        return rec(0, prices, 1, 0, dp);
    }
    public int rec(int i, int [] prices, int canb, int t, int[][][] dp){
        if(i==prices.length || t==2) return 0;
        if(dp[i][canb][t]!= -1)return dp[i][canb][t];
        int pick = 0, notPick = 0;
        if(canb==1) {
            pick = -prices[i] + rec(i+1, prices, 0, t, dp);
            notPick = rec(i+1, prices, 1, t, dp);
        } else {
            pick = prices[i] + rec(i+1, prices, 1, t+1, dp);
            notPick = rec(i+1, prices, 0, t, dp);
        }
        return dp[i][canb][t] = Math.max(pick, notPick);
    }
}