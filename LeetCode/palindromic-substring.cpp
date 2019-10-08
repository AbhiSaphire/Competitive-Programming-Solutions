/*
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
*/

class Solution {
public:
    string longestPalindrome(string s) {
        if(s.size() < 1)
            return "";
        int start=0, end=0;
        for(int i=0; i<s.size(); i++){
            int len1 = expand(s, i, i);
            int len2 = expand(s, i, i+1);
            int len = max(len1, len2);
            if(len > end -start){
                start = i - (len-1) / 2;
                end = i + len / 2;
            }
        }
        return s.substr(start, end+1);
    }
    
    int expand(string s, int left, int right){
        int L = left, R = right;
        while(L >= 0 && R < s.size() & s[L] == s[R]){
            L--; 
            R++;
        }
        return R - L - 1;
    }
    
};
