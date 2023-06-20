#include <algorithm>
#include <iostream>
#include <queue>
#include <vector>

#define INF 1e9
#define INFLL 1e18
using namespace std;
typedef pair<int, int> pint;
vector<pint> vertex[20009];
priority_queue<pint, vector<pint>, greater<pint> > pq;
int dist[20009];

int main() {
    int V, E, K;
    cin >> V >> E;
    cin >> K;

    int u, v, w;
    for (int i = 0; i < E; i++) {
        cin >> u >> v >> w;
        vertex[u].push_back({w, v});
    }

    fill(dist, dist + V + 1, INF);
    //---

    dist[K] = 0;
    pq.push({0, K});

    while (pq.size()) {
        auto [curd, cur] = pq.top();
        pq.pop();
        if (dist[cur] < curd) continue;
        for (int i = 0; i < vertex[cur].size(); i++) {
            auto [nxtd, nxt] = vertex[cur][i];
            if (dist[nxt] > curd + nxtd) {
                dist[nxt] = curd + nxtd;
                pq.push({dist[nxt], nxt});
            }
        }
    }

    for (int i = 1; i < V + 1; i++) {
        if (dist[i] == INF) {
            cout << "INF\n";
        } else {
            cout << dist[i] << "\n";
        }
    }
}