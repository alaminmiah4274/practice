#include <bits/stdc++.h>
using namespace std;


class Alphabet
{
public:
    char letter;
    int count;
};


bool custom_string_sort(Alphabet a, Alphabet b)
{
    if (a.count == b.count)
    {
        return a.letter < b.letter;
    }
    else 
    {
        return a.count > b.count;
    }

    
};


int main()
{
    string text;
    cin >> text;

    Alphabet count_arr[26];
    for (int i = 0; i < 26; i++)
    {
        count_arr[i].letter = char(i + 'a');
        count_arr[i].count = 0;
    }

    for (char e : text)
    {
        int ascii_value = int(e - 'a');
        count_arr[ascii_value].count++;
    }

    sort(count_arr, count_arr + 26, custom_string_sort);
    for (int i = 0; i < 26; i++)
    {
        if (count_arr[i].count > 0)
        {
            // cout << count_arr[i].letter << " " << count_arr[i].count << "\n";
            for (int j = 0; j < count_arr[i].count; j++)
            {
                cout << count_arr[i].letter;
            }
        }
    }


    return 0;
}