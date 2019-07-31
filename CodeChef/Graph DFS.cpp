#include <bits/stdc++.h>
using namespace std;
#define ll long long int
const int mn = 1e5+5;
vector<int> a[mn];
bool seen[mn] = {0};

void dfs(int u){
    seen[u] = 1;
    for (auto v : a[u]){
        if (!seen[v])
            dfs(v);
    }
}

int main(){
    int n,m; cin>>n>>m;
    int u,v;
    while(m--){
        cin>>u>>v;
        a[u].push_back(v);
        a[v].push_back(u);
    }
    int x; cin>>x;
    a[x].clear();
    seen[x] = 1;
    if(x!=0)
        dfs(0);
    else
        dfs(1);
    bool ok = true;
    for(int i=0;i<n;i++){
        if(!seen[i]){
            ok = false;
            break;
        }
    }
    if(!ok)
        cout<<"Not Connected";
    else
       cout<<"Connected";
    return 0;
}
