#include <bits/stdc++.h>
using namespace std;

// contest link: https://www.hackerrank.com/contests/xpsc-contest-a-batch-05/challenges 


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    
    int t;
    cin >> t;
    
    while (t--)
    {
        int n;
        cin >> n;
        cin.ignore();
        
        
        string str;
        cin >> str;
        
        int count = 0;
        for (auto i = 0; i < str.size() - 1; i++)
        {
            if ((str[i] == '0' && str[i + 1] == '1') || (str[i] == '1' && str[i + 1] == '0'))
            {
                count++;
            }
        }
        
        cout << count << "\n";
        
    }
    
    return 0;
}