class Solution {
public:
    int repeatedNTimes(vector<int>& A) {
       /* int C;
        vector<int> B;
        B.push_back(A[0]);
        for(int i =1; i<A.size();i++){
            
            for(int j = 0; j<B.size();j++){
                if(A[i] == B[j]){
                    C = B[j];
                    break;
                }
                B.push_back(A[i]);
                
            }
            
        }
        
        return C;
        */
        int C;
        for(int i =0; i<A.size();i++){
            C = A[i];
            for(int j = i+1; j<A.size();j++){
                if(C == A[j]){
                    return C;
                }
                
            }
        }
        return C;
    }
};