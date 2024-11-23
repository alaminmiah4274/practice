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


/*
#include <bits/stdc++.h>
using namespace std;

int main() {
    // your code goes here
    int n;
    cin >> n;

    string t;
    cin >> t;

    bool flag = true;
    if (n % 2 == 1)
    {
        int one = ((n + 1) / 2) - 1;
        for (int i = 0; i < one; i++)
        {
            if (t[i] != '1')
            {
                flag = false;
                break;
            }
        }


        int slash = ((n + 1) / 2);
        if (t[slash - 1] != '/')
        {
            flag = false;
        }

        int two = ((n + 1) / 2) + 1;
        for (int i = two - 1; i < n; i++)
        {
            if (t[i] != '2')
            {
                flag = false;
                break;
            }
        }
    }
    else
    {
        flag = false;
    }

    if (flag) cout << "Yes" << "\n";
    else cout << "No" << "\n";


    return 0;
}

*/