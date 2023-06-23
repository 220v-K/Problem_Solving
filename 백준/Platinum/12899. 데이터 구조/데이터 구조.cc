#include <algorithm>
#include <cmath>
#include <iostream>
#include <vector>

#define initialization cin.tie(0)->ios_base::sync_with_stdio(0);
using namespace std;

vector<int> tree;
vector<int> result;

int add(int s, int e, int idx, int X) {
    if (s == e) {
        return tree[idx] += 1;
    }
    int mid = (s + e) / 2;
    // X가 있는 쪽으로만 재귀.
    if (X <= mid)
        add(s, mid, idx * 2, X);
    else
        add(mid + 1, e, idx * 2 + 1, X);
    return tree[idx] = tree[idx * 2] + tree[idx * 2 + 1];
}

int del(int s, int e, int idx, int X) {
    if (s == e) {
        tree[idx] -= 1;
        return s;
    }

    int mid = (s + e) / 2;

    // leaf node에서부터 끌어올릴 Xth number.
    int num;
    // left child node보다 X가 작거나 같다면, 왼쪽 child node로 재귀.
    if (X <= tree[idx * 2]) num = del(s, mid, idx * 2, X);
    /* left child node보다 X가 크다면, 오른쪽 child node로 재귀.
    이 때, left child node의 숫자는 left child node의 child node에 포함된 숫자들의 개수이므로
    (더 작은 것이 그만큼 있는 것이니), 그만큼을 X에서 빼준다.*/
    else
        num = del(mid + 1, e, idx * 2 + 1, X - tree[idx * 2]);
    // 바뀐 leaf node의 parent node들 갱신.
    tree[idx] = tree[idx * 2] + tree[idx * 2 + 1];

    return num;
}

int main() {
    initialization;
    int N;
    cin >> N;

    int h = ceil(log2(2000000));
    int treeSize = 1 << (h + 1);
    tree.resize(treeSize);

    vector<int> result;

    for (int i = 0; i < N; i++) {
        int T, X;
        cin >> T >> X;

        if (T == 1) {
            add(0, 2000000 - 1, 1, X);
        } else {
            result.push_back(del(0, 2000000 - 1, 1, X));
        }
    }

    for (int i = 0; i < result.size(); i++) {
        cout << result[i] << "\n";
    }
}
