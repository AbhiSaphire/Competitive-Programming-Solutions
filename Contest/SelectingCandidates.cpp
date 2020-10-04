#include<bits/stdc++.h>
using namespace std;

int maxof3(int a, int b, int c){
	if (a >= b && a >= c)
		return a;
	else if (b >= a && b >= c)
		return b;
	else
		return c;
}

int minof3(int a, int b, int c){
	if (a <= b && a <= c)
		return a;
	else if (b <= a && b <= c)
		return b;
	else
		return c;
}

int main(){
	int t, n, val, best, worst;
	cin >> t;
	for (int i = 0; i < t; i++){
		cin >> n;
		queue <int> g;
		for (int j = 0; j < n; j++){
			g.push(j);
		}
		cout << "TRUE";
		while(true){
			if (g.size() == 1){
				val = g.front();
				best += val;
				worst += val;
				g.pop();
				break;
			}
			else if (g.size() == 2){
				val = g.front();
				g.pop();
				int val1 = g.front();
				g.pop();
				best += max(val, val1);
				worst += max(val, val1);
				break;
			}
			else{
				int f = g.front();
				g.pop();
				int s = g.front();
				g.pop();
				int t = g.front();
				g.pop();
				val = maxof3(f, s, t);
				int val1 = minof3(f, s, t);
				best += val1;
				worst += val;
			}
		}
		cout << best << " " << worst;
	}
	return 0;
}