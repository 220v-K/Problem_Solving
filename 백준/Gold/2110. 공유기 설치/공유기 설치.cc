#include <algorithm>
#include <iostream>
#include <vector>
#define init cin.tie(0)->ios_base::sync_with_stdio(0);

typedef long long ll;
const ll MAX = 1e10 + 1;

using namespace std;

vector<ll> arr;

int bs(ll gap) {
    int cnt = 1;
    ll tmp = 0;
    for (int i = 0; i < arr.size() - 1; i++) {
        if (arr[i + 1] - arr[i] + tmp >= gap) {
            tmp = 0;
            cnt++;
        } else {
            tmp += arr[i + 1] - arr[i];
        }
    }
    return cnt;
}

int main() {
    init;
    int N, C;
    cin >> N >> C;

    ll x;
    for (int i = 0; i < N; i++) {
        cin >> x;
        arr.push_back(x);
    }
    sort(arr.begin(), arr.end());

    ll lo, hi;
    for (int i = 0; i < N - 1; i++) {
        lo = min(lo, arr[i + 1] - arr[i]);
        hi = max(hi, arr[i + 1] - arr[i]);
    }

    ll result;
    while (lo <= hi) {
        ll mid = (lo + hi) / 2;

        ll k = bs(mid);
        if (k >= C) {
            result = mid;
            lo = mid + 1;
        } else if (k < C) {
            hi = mid - 1;
        }
    }

    cout << result;
}