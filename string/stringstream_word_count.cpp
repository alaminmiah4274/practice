#include <bits/stdc++.h>
using namespace std;


int main()
{
    string text;
    getline(cin, text);

    stringstream word_maker(text);
    string word;
    int word_count = 0;

    while (word_maker >> word)
    {
        word_count++;   
    }

    cout << word_count;



    return 0;
}