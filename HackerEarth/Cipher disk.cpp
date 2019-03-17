#include<iostream>
#include<string.h>
using namespace std;

int main(){
    int t, temp = 0;
    cin>>t;
    while(t--){
        string s;
        int prev=0,next=0;
        s.clear();
        cin>>s; 
        for(int i=0;s[i]!='\0';i++){
            temp=next;
            next=(s[i]-'a');
            prev=temp;
            if(next-prev <= -13) cout<<(next-prev+26)<<" ";
            else if(next-prev > 13) cout<<(next-prev-26)<<" ";
            else cout<<next-prev<<" ";
        }
        cout<<endl;
    }
    return 0;
}
