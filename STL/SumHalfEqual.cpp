#include <map>
#include <vector>
#include <unordered_map>
#include <iostream>

using namespace std;

int main(){
	int n = 3;
	//cin>> n;
	vector<int> A = {1, 2, 3};
	long long S = 0;

	//for (int i=0; i<n; i++)	cin>>A[i];
	for (int i=0; i<n; i++)	S += A[i];

	map<int, int> M1, M2;
	M1[A[0]] = 1;

	for (int i=0; i<n; i++)	M2[A[i]]++;
	
	int Sdash = 0;

	for (int i=0 ; i<=n; i++){
		Sdash += A[i];
		if(Sdash == S/2){
			cout<<"YES\n";
			return 0;
		}
		if (Sdash < S/2){
			long long x = S/2 - Sdash;
			if (M2[x] > 0){
				cout<<"Yes\n";
				return 0;
			}	
		}
		else{
			long long y = Sdash - S/2;
			if(M1[y] > 0){
				cout<<"Yes\n";
				return 0;
			}
		}
		M1[A[i+1]]++;
		M2[A[i+1]]--;
	}
	cout<<"No\n";
	return 0;
}
