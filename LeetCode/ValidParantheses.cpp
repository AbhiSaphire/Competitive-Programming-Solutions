class Solution {
public:
    bool isValid(string s) {
        stack<char> st;
        for(const auto c : s){
            switch(c){
                case('('):
                case('{'):
                case('['):
                    st.push(c);
                    break;
                case(')'):
                    if(st.empty() || st.top() != '(') return false;                    
                    else st.pop();                    
                    break;
                case('}'):
                    if(st.empty() || st.top() != '{') return false;
                    else st.pop(); 
                    break;
                case(']'):
                    if(st.empty() || st.top() != '[') return false;
                    else st.pop();
                    break;
                default:
                    return false;
            }
        }
        return st.empty();
    }
};
