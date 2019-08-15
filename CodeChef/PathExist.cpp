/*
Given a N X N matrix (M) filled with 1, 0, 2, 3. The task is to find whether there is a path possible from source to destination, while traversing through blank cells only. You can traverse up, down, right and left.

A value of cell 1 means Source.
A value of cell 2 means Destination.
A value of cell 3 means Blank cell.
A value of cell 0 means Blank Wall.

For each test case in a new line print 1 if the path exist from source to destination else print 0.
*/

#include<bits/stdc++.h>
using namespace std;
int A[20][20];
int x[] = {1,-1,0,0};
int y[] = {0,0,1,-1};
 bool vis[20][20];
int n;
bool valid(int xx,int yy){
    return xx>=0 and yy>=0 and xx<n and yy<n and !vis[xx][yy] and  A[xx][yy]==3;
}
int main()
 {
     int t;
      cin>>t;
      while(t--)
      {
        cin>>n;
      pair<int,int> s;
      pair<int,int> d;
      
      for(int i=0;i<n;i++){
      for(int j=0;j<n;j++){
      cin>>A[i][j];
      if(A[i][j]==1)
      s = {i,j};
      else if(A[i][j]==2)
      d = {i,j};
      }
      }
    bool ans =0;
    for(int i=0;i<20;i++)
    {
        for(int j=0;j<20;j++)
        {
            vis[i][j] = false;
        }
    }
    queue<pair<int,int> > q;
      q.push(s);
      while(!q.empty())
      {
          pair<int,int> tt = q.front();
          vis[tt.first][tt.second]=true;
          q.pop();
          for(int i=0;i<4;i++)
          {
              if(A[tt.first+x[i]][tt.second+y[i]]==2)
            {
              ans = 1;
              break;
            }
              if(valid(tt.first+x[i],tt.second+y[i])){
                q.push({tt.first+x[i],tt.second+y[i]});
              }
          }
          if(ans)
          break;
        
      }
      cout<<ans<<endl;
      
      }
    return 0;
}
