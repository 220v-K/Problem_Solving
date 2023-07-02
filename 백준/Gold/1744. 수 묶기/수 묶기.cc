#include <algorithm>
#include <iostream>
#include <vector>

#define init cin.tie(0)->ios_base::sync_with_stdio(0);
using namespace std;

typedef long long ll;

int main() {
    init;

    int N;
    cin >> N;

    vector<int> arr;
    int k;
    for (int i = 0; i < N; i++) {
        cin >> k;
        arr.push_back(k);
    }
    sort(arr.begin(), arr.end());

    ll result = 0;

    for (int i = N - 1; i >= 0; i--) {
        if (i == 0) {
            result += arr[i];
            continue;
        }
        if (arr[i] > 0 && arr[i - 1] > 0) {
            if (arr[i - 1] == 1) {
                result += arr[i];
                continue;
            }
            result += arr[i] * arr[i - 1];
            i--;
        } else if (arr[i] > 0 && arr[i - 1] == 0) {
            result += arr[i];
        } else if (arr[i] > 0 && arr[i - 1] < 0) {
            result += arr[i];
        } else if (arr[i] == 0 && arr[i - 1] < 0) {
            // 남은 음수의 개수가 짝수
            if (i % 2 == 0) continue;
            // 남은 음수의 개수가 홀수
            i--;
        } else if (arr[i] < 0 && arr[i - 1] < 0) {
            // 남은 음수의 개수가 짝수
            if (i % 2 == 1) {
                result += arr[i] * arr[i - 1];
                i--;
            } else {
                // 남은 음수의 개수가 홀수
                result += arr[i];
            }
        } else {
            result += arr[i];
        }
    }

    cout << result;
}