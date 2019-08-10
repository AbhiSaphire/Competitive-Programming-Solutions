#include <iostream>
using namespace std;

/*
On a positive integer, you can perform any one of the following 3 steps. 
1.) Subtract 1 from it. ( n = n - 1 ) 
2.) If its divisible by 2, divide by 2. ( if n % 2 == 0 , then n = n / 2  )
3.) If its divisible by 3, divide by 3. ( if n % 3 == 0 , then n = n / 3  ).
Now the question is, given a positive integer n, find the minimum number of steps that takes n to 1

eg: 1.)For n = 1 , output: 0       2.) For n = 4 , output: 2  ( 4  /2 = 2  /2 = 1 ) 
*/
int dynamicProgSolution(int n);
int memoizationSolution(int n, int memo[]);
int n;

int main(){
	cin>>n;
	int memo[n+1];
	int result1 = dynamicProgSolution(n);
	cout<<"result1  "<<result1<<endl;
	int result2 = memoizationSolution(n, memo);
	cout<<"result2  "<<result2<<endl;
	return 0;
}

int dynamicProgSolution(int n){
	int dp[n+1] ;
	dp[1] = 0;
	for(int i=2; i<=n; i++){
		dp[i] = 1 + dp[i-1];
		if(i % 2 == 0)	dp[i] = min(dp[i] , 1 + dp[n/2]);
		if(i % 3 == 0)	dp[i] = min(dp[i] , 1 + dp[n/3]);
	}
	return dp[n];
}

int memoizationSolution(int n, int memo[]){
	if(n == 1)	return 0;
	if(memo[n] != -1 ) return memo[n];
	int r = 1 + memoizationSolution( n - 1 , memo);
	if(n % 2 == 0)   r  =  min(r , 1 + memoizationSolution(n / 2 , memo)) ;
	if(n % 3 == 0)   r  =  min(r , 1 + memoizationSolution(n / 3 , memo)) ;
	memo[n] = r ;

	return r;
}
