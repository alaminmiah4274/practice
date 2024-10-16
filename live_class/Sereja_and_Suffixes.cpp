#include <bits/stdc++.h>
using namespace std;

// problem: https://codeforces.com/contest/368/problem/B 
// batch 4 contest: https://www.hackerrank.com/contests/xpsc-contest-a-batch-04/challenges

int main() {
   ios::sync_with_stdio(false);
   cin.tie(nullptr);

   int n, m;
   cin >> n >> m;
   vector<int> a(n + 1);
   for (int i = 1;i <= n;i++) {
      cin >> a[i];
   }

   vector<int> cnt(n + 1);
   set<int> s;
   for (int i = n;i >= 1;i--) {
      s.insert(a[i]);
      cnt[i] = s.size();
   }

   for (int i = 1;i <= m;i++) {
      int pos;
      cin >> pos;
      cout << cnt[pos] << '\n';
   }

   return 0;
}