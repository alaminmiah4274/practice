#include <bits/stdc++.h>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;

    while (T--)
    {
        int n, k;
        cin >> n >> k;
        
        vector<int> a(n);
        unordered_map<int, int> freq;

        for (int i = 0; i < n; ++i)
        {
            cin >> a[i];
            if (a[i] <= n)
            {
                freq[a[i]]++; 
            }
        }

        int missingCount = 0;
        for (int i = 1; i <= n; ++i)
        {
            if (freq[i] == 0)
            {
                missingCount++; 
            }
        }

        
        if (missingCount <= k)
        {
            cout << "YES\n";
        } 
        else 
        {
            cout << "NO\n";
        }
    }
    
    
    return 0;
}
