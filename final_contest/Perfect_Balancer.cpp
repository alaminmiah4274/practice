#include <bits/stdc++.h>
#define ll long long 
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    
    int n;
    cin >> n;
    
    vector<int> nums(n);
    for (int i = 0; i < n; i++)
    {
        cin >> nums[i];
    }
    
    vector<ll> pre(n);
    pre[0] = nums[0];
    for (int i = 1; i < n; i++)
    {
        pre[i] = nums[i] + pre[i - 1];
    }
    
    
    
    bool not_unstable = false;
    ll balancer_module = INT_MAX;
    int index_value = INT_MAX;
    for (int i = 0; i < n; i++)
    {
        
        ll sum1;
        if (i == 0)
        {
            sum1 = pre[i];
        }
        else 
        {
            sum1 = pre[i];
        }
        
        
        ll sum2;
        if (i == 0)
        {
            sum2 = pre[n - 1];
        }
        else 
        {
            sum2 = pre[n - 1] - pre[i - 1];
        }

        
        
        if (sum1 == sum2)
        {
            not_unstable = true;
            balancer_module = sum1;
            index_value = i + 1;
            break;
        }
    }
    
    
    if (not_unstable) cout << balancer_module << " " << index_value << "\n";
    else cout << "UNSTABLE" << "\n";
    
    return 0;
}