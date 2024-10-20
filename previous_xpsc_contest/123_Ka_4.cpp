#include <bits/stdc++.h>
using namespace std;


// contest link: https://www.hackerrank.com/contests/xpsc-contest-a-batch-04/challenges 


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int n;
    cin >> n;
    
    for (int i = 1; i <= n; i++)
    {
        if (i == 1)
        {
            for (int j = 1; j <= n; j++)
            {
                cout << j;
            }
            cout << endl;
        }
        else if (i > 1 && i < n)
        {
            cout << i;
            for (int j = 1; j <= n - 2; j++)
            {
                cout << " ";
            }
            cout << n;
            cout << endl;
        }
        else if (i == n)
        {
            for (int i = 1; i <= n; i++)
            {
                cout << n;
            }
        }
    }
    
    return 0;
}