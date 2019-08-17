#include <bits/stdc++.h>
using namespace std;
int A[101][101];
void changecolor(int x, int y, int c, int n, int m);

int main() {
	int t;
	cin>>t;
	while(t--){
	    int n, m;
	    cin>>n>>m;
	    for(int i=0; i<n; i++){
	        for(int j=0; j<m; j++){
	            cin>>A[i][j];
	        }
	    }
	    int x, y, c;
	    cin>>x>>y>>c;
	    changecolor(x, y, c, n, m);
	}
	return 0;
}

void changecolor(int x, int y, int c, int n, int m){
    int vis[n][m];
    for(int i=0; i<n; i++){
        for(int j=0; j<m; j++){
            vis[i][j] = -1;
        }
    }
    queue <pair<int, int>> Q;
    Q.push(make_pair(x, y));
    vis[x][y] = 1;
    
    while(!Q.empty()){
        pair<int, int> ipair = Q.front();
        Q.pop();
        int t = A[ipair.first][ipair.second];
        A[ipair.first][ipair.second] = c;
        if(ipair.first-1>=0 && ipair.first-1<n && A[ipair.first-1][ipair.second] == t && vis[ipair.first-1][ipair.second] == -1){
            Q.push(make_pair(ipair.first-1, ipair.second));
            vis[ipair.first-1][ipair.second] = 1;
        }
        if(ipair.first+1>=0 && ipair.first+1<n && A[ipair.first+1][ipair.second] == t && vis[ipair.first+1][ipair.second] == -1){
            Q.push(make_pair(ipair.first+1, ipair.second));
            vis[ipair.first+1][ipair.second] = 1;
        }
        if(ipair.second-1>=0 && ipair.second-1<n && A[ipair.first][ipair.second-1] == t && vis[ipair.first][ipair.second-1] == -1){
            Q.push(make_pair(ipair.first, ipair.second-1));
            vis[ipair.first][ipair.second-1] = 1;
        }
        if(ipair.second+1>=0 && ipair.second+1<n && A[ipair.first][ipair.second+1] == t && vis[ipair.first][ipair.second+1] == -1){
            Q.push(make_pair(ipair.first, ipair.second+1));
            vis[ipair.first][ipair.second+1] = 1;
        }
    }
    
    for(int i=0; i<n; i++){
        for(int j=0; j<m; j++){
            cout<<A[i][j]<<" ";
        }
    }
    cout<<endl;
}
