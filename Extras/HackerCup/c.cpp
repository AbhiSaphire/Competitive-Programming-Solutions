#include<bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace __gnu_pbds;
using namespace std;

#define mod 1000000007
#define lli long long
#define fi first
#define se second
#define pb emplace_back
#define FOR(i,n) for(int i=0;i<n;i++)
#define FORR(x,v) for(auto x : v)
#define ordered_set tree<int, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update>
#define MAXC 800005
// %

int n, m, i, j, t, q, ok, cnt;
lli k, r, x, y, z, ans, P[MAXC], H[MAXC];
string s, c;

int main(int argc, char **argv)
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> t;
    for(q=1;q<=t;q++, ans=0){
        cin >> n;
        FOR(i, n){
            cin >> P[i] >> H[i];
        }
        vector< int > ord(n);
        iota(ord.begin(), ord.end(), 0);
        sort(ord.begin(), ord.end(), [&](int i, int j){
            return P[i] < P[j];
        });
        map< lli, lli > L, R;
        FORR(i, ord){
            if(R.count(P[i])){
                R[P[i]+H[i]] = R.count(P[i] + H[i])? min(R[P[i]+H[i]], R[P[i]]) : R[P[i]] ;
            }
            else{
                R[P[i]+H[i]] = R.count(P[i] + H[i])? min(R[P[i]+H[i]], P[i]) : P[i] ;
            }
            ans = max(ans, abs(R[P[i]+H[i]] - (P[i] + H[i])));
        }
        reverse(ord.begin(), ord.end());
        FORR(i, ord){
            if(L.count(P[i])){
                L[P[i]-H[i]] = L.count(P[i] - H[i])? max(L[P[i]-H[i]], L[P[i]]) : L[P[i]] ;
            }
            else{
                L[P[i]-H[i]] = L.count(P[i] - H[i])? max(L[P[i]-H[i]], P[i]) : P[i] ;
            }
            ans = max(ans, abs(L[P[i]-H[i]] - (P[i] - H[i])));
        }
        FORR(x, L){
            if(R.count(x.fi)){
                ans = max(ans, abs(x.se - x.fi) + abs(R[x.fi] - x.fi));
            }
        }
        cout << "Case #" << q << ": " << ans << '\n';
    }
}