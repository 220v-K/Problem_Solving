#include <algorithm>
#include <cmath>
#include <iostream>
#include <vector>

#define initialization cin.tie(0)->ios_base::sync_with_stdio(0);
using namespace std;

const long long INTF = 1e9 + 7;

vector<long long> tree;
vector<long long> num;
vector<long long> result;

long long init(int s, int e, int idx) {
    if (s == e) return tree[idx] = num[s];
    int mid = (s + e) / 2;
    return tree[idx] = (init(s, mid, idx * 2) * init(mid + 1, e, idx * 2 + 1)) % INTF;
}

long long mul(int s, int e, int l, int r, int idx) {
    if (l > e || r < s) return 1;
    if (l <= s && e <= r) return tree[idx];

    int mid = (s + e) / 2;
    return (mul(s, mid, l, r, idx * 2) * mul(mid + 1, e, l, r, idx * 2 + 1)) % INTF;
}

long long update(int s, int e, int idx, int num, long long now) {
    if (num < s || num > e) return tree[idx];
    if (s == e) return tree[idx] = now;
    int mid = (s + e) / 2;
    return tree[idx] = (update(s, mid, idx * 2, num, now) * update(mid + 1, e, idx * 2 + 1, num, now)) % INTF;
}

int main() {
    initialization;
    int N, M, K;
    cin >> N >> M >> K;

    long long n;
    for (int i = 0; i < N; i++) {
        cin >> n;
        num.push_back(n);
    }

    int h = ceil(log2(N));
    int treeSize = 1 << (h + 1);
    tree.resize(treeSize);

    init(0, N - 1, 1);

    int a, b;
    long long c;
    for (int i = 0; i < M + K; i++) {
        cin >> a >> b >> c;
        if (a == 1) {
            num[b - 1] = c;
            update(0, N - 1, 1, b - 1, c);
        } else if (a == 2) {
            result.push_back(mul(0, N - 1, b - 1, c - 1, 1));
        }
    }

    for (int i = 0; i < result.size(); i++) {
        cout << result[i] << "\n";
    }
}