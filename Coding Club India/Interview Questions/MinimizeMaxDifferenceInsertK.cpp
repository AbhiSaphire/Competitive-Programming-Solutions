#include <bits/stdc++.h>
using namespace std;

int minimizedMaxDiff(int arr[], int n, int k){
        int maxx = INT_MIN;
        for (int i = 0; i < n - 1; i++) 
            maxx = max(maxx, abs(arr[i] - arr[i + 1])); 
        
        if (maxx == 0) 
            return 0;
            
        int low = 1; 
        int high = maxx; 
        int mid, temp; 
      
        while (low < high){
            mid = (low + high) / 2; 
            temp = 0; 
            for (int i = 0; i < n - 1; i++){ 
                temp += (abs(arr[i] - arr[i + 1])- 1) / mid; 
            } 
            if (temp > k) 
                low = mid + 1;
            else
                high = mid; 
        } 
        return high;
}

int main(){
    int arr[] = {66, 31, 99, 76, 38, 76};
    int res = minimizedMaxDiff(arr, 6, 5);
    cout << res << endl;
    return 0;
}