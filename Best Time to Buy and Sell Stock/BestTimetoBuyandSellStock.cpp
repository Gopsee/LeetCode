class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int days = prices.size();
        if(days == 0)
            return 0;
        int min=prices[0];
        int best=0;
        // high=0;
        //int lowest=0;
        for(int j =0; j<=days-1; j++){
            if (min>prices[j])
                min=prices[j];
            else
                best = max(best, prices[j]-min);
            
            
            // if(prices[j]<min)
            //    min = prices[j];
            //else if(prices[j] - min > best)
              //  best = prices[j]-min;
            }
            //high = max(high,prices[i]);
            //lowest = min(lowest,prices[i]);
            //best = high - lowest;
                   
        
        return best;
    }
};