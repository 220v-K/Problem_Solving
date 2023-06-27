#include <algorithm>
#include <iostream>
#include <vector>
#define init cin.tie(0)->ios_base::sync_with_stdio(0);

typedef long long ll;
const ll MAX = 1e9 + 3;

using namespace std;

ll dp[1002][1002];

int main() {
    init;

    for (int i = 0; i < 1001; i++) {
        dp[i][0] = 1;
        dp[i][1] = i;
    }

    for (int i = 2; i < 1001; i++) {
        for (int j = 2; j < 1001; j++) {
            dp[i][j] = (dp[i - 2][j - 1] + dp[i - 1][j]) % MAX;
        }
    }

    int N, K;
    cin >> N >> K;
    cout << (dp[N - 3][K - 1] + dp[N - 1][K]) % MAX;
}