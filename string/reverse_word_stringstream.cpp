#include <bits/stdc++.h>
using namespace std;


void reverse_word(stringstream &word_maker)
{
    string word;
    if (word_maker >> word)
    {
        reverse_word(word_maker);
        cout << word << "\n";
    }
}

int main()
{
    string text;
    getline(cin, text);

    stringstream word_maker(text);
    reverse_word(word_maker);



    return 0;
}