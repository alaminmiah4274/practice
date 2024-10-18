#include <bits/stdc++.h>
using namespace std;

// contest link: https://www.hackerrank.com/contests/xpsc-final-contest-a-batch-05 


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    
    int t;
    cin >> t;

    while (t--) {
        int n, k;
        cin >> n >> k;
        cin.ignore();

        string a_str, b_str;
        cin >> a_str >> b_str;

        long long int count = 0;
        for (int i = 0; i < n; i++) 
        {
            if (a_str[i] != b_str[i])
            {
                count++;
            }
        }

        if (count <= k) 
            cout << "YES" << "\n";
        else 
            cout << "NO" << "\n";
    }
    
    return 0;
}
