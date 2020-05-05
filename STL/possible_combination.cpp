// ~~ABHISHEK K. SINGH~~
// Time complexity -- O(n*n!) ---> O(n)/result and n! results
// Auxilary space -- O(1)

#include<bits/stdc++.h>
using namespace std;

void solution(string str, string out){
	if(str.size() == 0){
		cout << out << endl;
		return;
	}
	for(int i=0; i<str.size(); ++i){
		solution(str.substr(1), out + str[0]);
		rotate(str.begin(), str.begin()+1, str.end());
	}
}

int main(){
	string str = "ABHISHEK";
	solution(str, "");
	return 0;
}
