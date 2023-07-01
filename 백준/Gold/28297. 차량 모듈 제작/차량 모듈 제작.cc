#include <math.h>

#include <algorithm>
#include <cmath>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <stack>
#include <tuple>
#include <vector>

#define init cin.tie(0)->ios_base::sync_with_stdio(0);

using namespace std;

typedef long long ll;
typedef pair<int, int> pint;
typedef tuple<int, int, int> iii;
typedef pair<ll, ll> pll;

int parent[1004];

int N;
vector<iii> cir;

int find(int x) {
    if (parent[x] == x)
        return x;
    else
        return parent[x] = find(parent[x]);
}

bool _union(int x, int y) {
    x = find(x);
    y = find(y);
    if (x == y) return false;

    parent[min(x, y)] = max(x, y);
    return true;
}

double distance(int x1, int y1, int x2, int y2) {
    return sqrt(pow(y2 - y1, 2) + pow(x2 - x1, 2));
}

double beltDist(iii cir1, iii cir2) {
    int x1, y1, r1, x2, y2, r2;
    if (get<2>(cir1) > get<2>(cir2)) {
        x1 = get<0>(cir1);
        y1 = get<1>(cir1);
        r1 = get<2>(cir1);
        x2 = get<0>(cir2);
        y2 = get<1>(cir2);
        r2 = get<2>(cir2);
    } else {
        x1 = get<0>(cir2);
        y1 = get<1>(cir2);
        r1 = get<2>(cir2);
        x2 = get<0>(cir1);
        y2 = get<1>(cir1);
        r2 = get<2>(cir1);
    }

    double d = distance(x1, y1, x2, y2);
    double x = sqrt(pow(d, 2) - pow(r1 - r2, 2));
    double theta = asin((r1 - r2) / d);

    double res = 2 * x + r2 * (M_PI - 2 * theta) + r1 * (M_PI + 2 * theta);
    return res;
}

int main() {
    init;

    for (int i = 0; i < 1004; i++) {
        parent[i] = i;
    }
    cin >> N;
    int x, y, r;
    for (int i = 0; i < N; i++) {
        cin >> x >> y >> r;
        cir.push_back({x, y, r});
    }

    // 거리 측정 후 이미 닿아 있는 원은 union.
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (i == j) continue;
            double dis = distance(get<0>(cir[i]), get<1>(cir[i]), get<0>(cir[j]), get<1>(cir[j]));
            if (dis <= get<2>(cir[i]) + get<2>(cir[j])) {
                _union(i, j);
            }
        }
    }

    double v[N][N];

    // 모든 점 사이의 거리를 측정 (이미 연결된 원 제외))
    vector<tuple<double, int, int>> edges;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (i == j || find(i) == find(j)) continue;
            edges.push_back({beltDist(cir[i], cir[j]), i, j});
        }
    }
    // 거리순 오름차순 정렬
    sort(edges.begin(), edges.end());

    double res = 0;
    // Kruskal(MST)
    for (int i = 0; i < edges.size(); i++) {
        double dist = get<0>(edges[i]);
        int v1 = get<1>(edges[i]);
        int v2 = get<2>(edges[i]);

        if (find(v1) != find(v2)) {
            res += dist;
            _union(v1, v2);
        }
    }

    cout.precision(20);
    cout << res;
}