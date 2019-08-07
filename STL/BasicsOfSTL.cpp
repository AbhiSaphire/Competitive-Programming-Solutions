#include <iostream>
#include <vector>
#include <set>
#include <climits>
#include <algorithm>
#include <map>
using namespace std;

bool f(int x, int y){
	x > y;
}

// Some basic use of Vector in C++

void vectorFunction(){
	std::vector<int> v = {11, 2, 3, 4};
	cout << v[2] <<endl; 

	sort(v.begin(), v.end());
	bool present = binary_search(v.begin(), v.end(), 3); cout << present<<endl; //true, 1
	present = binary_search(v.begin(), v.end(), 5); cout<< present<<endl; //false, 0 

	v.push_back(200);
	present = binary_search(v.begin(), v.end(), 200); cout<<present<<endl; //true, 1

	v.push_back(200);
	v.push_back(200);
	v.push_back(200);
	v.push_back(200);
	v.push_back(200);
	v.push_back(230);
	//11, 2, 3, 4, 200, 200, 200, 200, 200, 200, 230

	auto it = lower_bound(v.begin(), v.end(), 200);
	auto it2 = upper_bound(v.begin(), v.end(), 200);

	cout<< *it << " " << *it2 <<endl; // 200, 230
	cout<< it2 - it <<endl; //6

	sort(v.begin(), v.end(), f);

	for(int &x: v){ //reference
		x+=2; 
	}

	for(int x: v){
		cout<<x<<" ";
	}
	cout<<endl;

}

//Some basic use of Sets in C++

void setFunction(){
	set<int> s;
	s.insert(1);
	s.insert(2);
	s.insert(3);
	s.insert(-1);

	for(int x: s){
		cout<<x<< " ";
	}
	cout<<endl;

	auto it4 = s.find(-1);
	if(it4 == s.end()){
		cout<<"not found "<<endl;
	}
	else{
		cout<<"found "<<*it4<<endl;
	}

	auto it = s.upper_bound(-1);
	auto it2 = s.upper_bound(2);
	cout<< *it << " " <<*it2 <<endl;

	cout<<endl;
}

//some basic use of maps in C++

void mapFUnction(){
	std::map<char, int> A;
	string x = "abhishek kumar";

	for(char c: x){
		A[c]++;
	}

	cout<<A['a'] << " " <<A['k']<<endl;
	cout<<endl;
}


int main(){

	vectorFunction();
	setFunction();
	mapFUnction();


/*
	Let you have been given a pair of numbers and then you have given a point, then you
	have to fu=ind in which pair this point belongs to.

	A simple aproach using C++ STL sets< pair<int, int> >
*/


	set< pair<int, int> > s;
	s.insert({1, 5});
	s.insert({6, 12});
	s.insert({20, 50});
	s.insert({60, 400});
	s.insert({601, 700});
	s.insert({701, 750});

	int point;
	cout<<"Enter Number :: ";
	cin>>point;
		auto it = s.upper_bound({point, INT_MAX});
		if(it ==  s.begin()){
			cout<<"OOPS.. Not Found!!";
			return 0;
		}
		it--;
		pair<int, int> current = *it;
		if(current.first < point && point <= current.second){
			cout<<"Yes it is present "<< current.first << " , " << current.second<<endl;
		}
		else{
			cout<<"OOPS.. Not Found!!";
		}

}
