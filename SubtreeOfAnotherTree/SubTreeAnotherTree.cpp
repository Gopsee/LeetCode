/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution{
    public:
    bool isidentical(TreeNode* s, TreeNode* t)
    {
        if(s==NULL&&t==NULL)
            return true;
        else if(s==NULL||t==NULL)
            return false;

        else
            return ((s->val==t->val)&&isidentical(s->left,t->left)&&isidentical(s->right,t->right));
    }


    bool isSubtree(TreeNode* s, TreeNode* t) {
       if(s==NULL)
          return false;

       if(s->val==t->val)
      {
          if(isidentical(s,t)) return true;
      }
       if(isSubtree(s->left,t)||isSubtree(s->right,t))
           return true;
        return false;
    }
};