#include <bits/stdc++.h>
using namespace std;

int main() {
    long long int n, q;
    cin >> n >> q;

    long long int pain_sum[n];
    // long long int half = n / 2;
    for (long long int i = 0; i < n / 2; i++)
    {
        pain_sum[2 * i] = i + 1;
        pain_sum[2 * i + 1] = i + 1;
    }

    long long int pre[n];
    pre[0] = pain_sum[0];
    for (long long int i = 1; i < n; i++)
    {
        pre[i] = pain_sum[i] + pre[i - 1];
    }
    

    

    while (q--) {
        long long int L, R;
        cin >> L >> R;

        L--;
        R--;

        long long int sum;
        if (L == 0)
        {
            sum = pre[R];
        } 
        else 
        {
            sum = pre[R] - pre[L - 1];
        }

        cout << sum << "\n";
    }

    return 0;
}