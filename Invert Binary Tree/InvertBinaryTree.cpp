/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {
        if(root == NULL){
            return NULL;
        }
        if(root->left == NULL && root->right == NULL){
            return root;
        }
        
        TreeNode* R = invertTree(root->right);
        TreeNode* L = invertTree(root->left);
        root->left = R;
        root->right = L;
        
        return root;
    }
};