#include <iostream>
using namespace std;

int main() {
	int t;
	cin>>t;
	while(t--){
	    int n, k, v;
	    cin>>n>>k>>v;
	    int array[n];
	    for (int i=0; i<n; i++){
	        cin>>array[i];
	    }
	    int sum=0;
	    for(int i=0; i<n; i++){
	        sum = sum + array[i];
	    }
	    int x = v * (k + n);
	    int l = x - sum;
	    if(l>0){
	        if(l%k == 0){
    	        int p = l/k;
    	        cout<<p<<endl;
    	    }
    	    else
    	        cout<<-1<<endl;
	    }
	    else
	        cout<<-1<<endl;
	}
	return 0;
}
