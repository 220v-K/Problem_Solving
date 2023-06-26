#include <algorithm>
#include <iostream>
#include <vector>
#define init cin.tie(0)->ios_base::sync_with_stdio(0);

typedef long long ll;
const ll MAX = 1e16 + 10;

using namespace std;

vector<ll> result;

int main() {
    init;

    ll a = 1;
    ll d = 3;

    int T;
    ll n;
    cin >> T;
    for (int k = 0; k < T; k++) {
        cin >> n;

        if (n == 1) {
            result.push_back(1);
            continue;
        }

        ll section = 0;

        ll lo = 0, hi = ll(1e9);
        while (lo <= hi) {
            ll mid = (lo + hi) / 2;
            ll S = mid * (3 * mid - 1) / 2;

            if (S >= n) {
                section = mid;
                hi = mid - 1;
            } else {
                lo = mid + 1;
            }
        }

        ll p = section - 1;
        n -= p * (3 * p - 1) / 2;

        ll line = 2 + (section - 2) * 3;

        ll total = (1 + line) * line / 2;

        if (n <= section - 1) {
            total = total + 2 + (n - 1) * 3;
        } else if (n <= section * 2 - 1) {
            total = total + (line + 1) + 1 + (n - (section - 1) - 1) * 3;
        } else {
            total = total + (line + 1) + (line + 2) + 3 + (n - (section * 2 - 1) - 1) * 3;
        }

        result.push_back(total);
    }

    for (int k = 0; k < result.size(); k++) {
        cout << result[k] << "\n";
    }

    return 0;
}