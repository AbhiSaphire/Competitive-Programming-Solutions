#include<bits/stdc++.h>
using namespace std;
class SortedStack{
public:
	stack<int> s;
	void sort();
};
void printStack(stack<int> s)
{
    while (!s.empty())
    {
        printf("%d ", s.top());
       	s.pop();
    }
    printf("
");
}
int main()
{
int t;
cin>>t;
while(t--)
{
	SortedStack *ss = new SortedStack();
	int n;
	cin>>n;
	for(int i=0;i<n;i++)
	{
	int k;
	cin>>k;
	ss->s.push(k);
	}
	ss->sort();
	printStack(ss->s);
}
}
}
/*This is a function problem.You only need to complete the function given below*/
/*The structure of the class is
class SortedStack{
public:
	stack<int> s;
	void sort();
};
*/
/* The below method sorts the stack s 
you are required to complete the below method */
void SortedStack :: sort(){
                                                                     / / /*    if(!s.empty()){
                                                                                  int temp = s.top(); s.pop();
                                                                                  sort();
                                                                                  sortedStack(s, temp);
                                                                              }
                                                                          }
                                                                          void sortedStack(stack<int> s, temp){
                                                                                  if(s.empty() || s.top() < temp){
                                                                                      s.push(temp);
                                                                                  }
                                                                                  else{
                                                                                      int temp2 = s.top(); s.pop();
                                                                                      sortedStack(s, temp);
                                                                                      s.push(temp2);
                                                                                  }*/ / / 
    //ACTUAL SOLUTION FROM HERE TC - O(n), SC - O(n)
    vector<int> vec;
    while(!s.empty()){
        vec.push_back(s.top());
        s.pop();
    }
    std::sort(vec.begin(), vec.end());
    int n = vec.size();
    for(int i = 0; i < n; i++)
    s.push(vec[i]);
}
