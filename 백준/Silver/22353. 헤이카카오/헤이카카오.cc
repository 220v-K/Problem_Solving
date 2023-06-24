#include <algorithm>
#include <cmath>
#include <iostream>
#include <vector>

#define initialization cin.tie(0)->ios_base::sync_with_stdio(0);
using namespace std;

int main() {
    initialization;

    double a;
    double d, k;
    cin >> a >> d >> k;
    d /= 100;
    k /= 100;

    double com = d * k;

    double result = 0.0;
    double last = 1.0;

    for (int i = 1; d <= 1; i++) {
        result += a * i * last * d;

        if (d >= 1) break;

        last *= 1 - d;
        d += d * k;
        if (d >= 1) d = 1;
    }

    cout.precision(10);
    cout << result;
}