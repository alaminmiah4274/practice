#include <bits/stdc++.h>
using namespace std;


int main()
{
    string line = "I am the best";
    string line2 = " progrmmer";

    // line += line2;
    // line.append(line2);

    // line.push_back('P');
    // line.pop_back();


    // line = "I am learning new things regularly";
    // line.assign("I am the best Software Engineer");

    // line.erase(6);
    // line.erase(4, 4);

    // line.replace(4, 2, "good");
    line.insert(13, " Programmer");

    cout << line << "\n";


    return 0;
}