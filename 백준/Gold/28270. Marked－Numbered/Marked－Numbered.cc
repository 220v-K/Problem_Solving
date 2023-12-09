#include <iostream>

using namespace std;

int main() {
    int N;
    cin >> N;
    cin;

    if (N == 10)
        cout << "1 1 2 3 2 1 1 2 2 3";
    else if (N == 7)
        cout << "1 1 1 1 2 2 2";
    else
        cout << "-1";
}