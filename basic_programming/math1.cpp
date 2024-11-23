#include <bits/stdc++.h>
using namespace std;

int main()
{
	double x, y, x_plus_y, x_minus_y;
	cin >> x_plus_y >> x_minus_y;

	x = (x_plus_y + x_minus_y) / 2;
	y = (x_plus_y - x_minus_y) / 2;

	cout << x << " " << y << "\n";


	return 0;
}