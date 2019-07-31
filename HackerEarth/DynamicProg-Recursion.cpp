#include <iostream>
using namespace std;
int array[] = {1, 10, 25};
int N = 2;
int getchange(int, int);
int min(int, int);

int main(){
	int changes = getchange(33, N);
	cout<<"changes of currency = ",changes;
	return 0;
}
int res = 0;
int inc, exc = 0;
int getchange(int change, int N){
	if(change == 0)
		return res;
	else if(array[N] <= change){
		inc = 1 + getchange(change-array[N], N);
		exc = getchange(change, N--);
		res = min(inc, exc);
	}
	else{
		exc = getchange(change, N--);
		res = exc;
	}
	return res;
}

int min(int a, int b){
	if(a<b)
		return a;
	else
		return b;
}
