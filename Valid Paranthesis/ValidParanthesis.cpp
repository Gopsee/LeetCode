class Solution {
public:
    bool isValid(string s) {
        if(s.size() == 0) 
            return true;
	
		stack<char> stk;
		unordered_map<char,char> mp;
        mp.insert({'(', ')'}); 
        mp.insert({'{', '}'});
        mp.insert({'[', ']'});

        for(auto & ch : s) {
			if(stk.size()) {
			    if(ch == mp[stk.top()]) 
                    stk.pop();
				else if(close(ch)) 
					return false;
				else
					stk.push(ch);
			}
			
            else if(close(ch)) 
				return false;
            else
				stk.push(ch);
        }
		
        return stk.size() == 0;
    }
	
    bool close(char c) {
        return  (c == ')' || c == '}' || c == ']');  
    }
};