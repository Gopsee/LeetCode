class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int temp;
        for(int row =0; row<matrix.size();row++){
            for(int col =0; col<matrix[0].size();col++){
                temp = matrix[col][row];
                matrix[col][row] = matrix[row][col];
                matrix[col][row] = temp;
            }            
        }
         
    }
};