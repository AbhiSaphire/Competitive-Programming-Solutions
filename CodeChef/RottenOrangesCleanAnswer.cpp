//This is the real solution given by GeeksforGeeks for Rotten Oranges question.
//If you want to have a look at my solution, go back and have a look at RottenOranges.cpp

#include <iostream>
#include <queue>
using namespace std;
#define pair <int, int> ipair;

bool isValid(int array[][100]);
void bfs(int array[][100], queue<ipair> *que, int *time_frame);

int main() {
	int t;
	queue<ipair> que;
	cin>>t;
	while(t--){
	    int r, c, time_frame;
	    cin>>r>>c;
	    int array[r][c];
	    for(int i=0; i<r; i++){
	        for(int j=0; j<c; j++){
	            cin>>array[r][c];
	            if(array[r][c] == 2){
	                que.push(make_pair(r,c));
	            }
	        }
	    }
	    que.push(make_pair(-1, -1));
	    while(!que.empty()){
	        bfs(array, &que, &time_frame);
	        ipair new1 = que.front();
	        ipair new2 = que.back();
	        if(new1.first == -1 && new1.second == -1 && que.front() != que.back()){
	            break;
	        }
	    }
	    if(time_frame != 0)
	        cout<<time_frame;
	    else
	        cout<<-1;
	}
	return 0;
}


bool isValid(int array[i][j]){
    if(i >= 0 && j >= 0 && i<r && j<c && array[i][j] == 1){
        return true;
    }
    else
        return false;
}

void bfs(int array[][], queue<ipair> *que, int *time_frame){
    ipair new = que.front();
    que.pop();
    if(new.first == -1 && new.second == -1){
        time_frame++;
    }
    if(isValid(array[new.first-1][new.second])){
        que.push(make_pair(new.first-1, new.second));
    }
    if(isValid(array[new.first+1][new.second])){
        que.push(make_pair(new.first+1, new.second));
    }
    if(isValid(array[new.first][new.second-1])){
        que.push(make_pair(new.first, new.second-1));
    }
    if(isValid(array[new.first-1][new.second+1])){
        que.push(make_pair(new.first, new.second+1));
    }
}
