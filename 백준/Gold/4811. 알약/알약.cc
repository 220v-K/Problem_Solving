#include <algorithm>
#include <iostream>
#include <vector>
#define init cin.tie(0)->ios_base::sync_with_stdio(0);

typedef long long ll;
using namespace std;

// dp[w][h] - w의 개수와 h의 개수일 때의 경우의 수 값.
ll dp[31][31];

ll dfs(int w, int h) {
    // h == -1이 되었다면,
    if (h == -1) return 0;
    // w == 0이면 모두 반개짜리만 남은 것 -> 경우의 수 1가지
    if (w == 0) return 1;

    if (dp[w][h] == 0)
        return dp[w][h] = dfs(w - 1, h + 1) + dfs(w, h - 1);
    else
        return dp[w][h];
}

int main() {
    init;

    while (1) {
        int n;
        cin >> n;
        if (n == 0) break;
        cout << dfs(n, 0) << "\n";
    }
}