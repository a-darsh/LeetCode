class Solution {
public:
    bool isValid(string s) {
        stack<char> stck;
        int i;
        char c;
        
        if(s.length()==0)
          return true;
        if(s.length()==1)
          return false;
        for(i=0;i<s.length();i++)
        {
            if((s[i]=='(') || (s[i]=='{') || (s[i]=='['))
                stck.push(s[i]);
            else 
            {
                if(stck.size()==0)
                  return false;
                switch(s[i])
                {
                  case ')':
                    if(stck.top()!='(')
                      return false;
                    break;
                    
                  case '}':
                    if(stck.top()!='{')
                      return false;
                    break;
                    
                  case ']':
                    if(stck.top()!='[')
                      return false;
                    break;
                }
              
                stck.pop();
            }
        }
            
        if(!stck.empty())
            return false;
        else
          return true;
    }
};