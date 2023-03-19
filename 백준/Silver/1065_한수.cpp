#include <iostream>

using namespace std;

int main()
{
    int a;
    cin >> a;

    if (0 < a && a < 100)
        cout << a;
    else if (100 <= a && a < 1000)
    {
        int num_sequence = 0;
        int first, second, third;
        for (int i=100; i <= a; i++)
        {
            first = i / 100;
            second = (i - first*100) / 10;
            third = (i - first*100 - second*10);

            if ((first - second) == (second - third))
                num_sequence++;
        }
        cout << num_sequence + 99;
    }
    else if (a == 1000)
        cout << 144;
    else
        cout << "undefined input";
}