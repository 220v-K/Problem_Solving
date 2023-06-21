#include <algorithm>
#include <iostream>
#include <queue>
#include <vector>

#define init cin.tie(0)->ios_base::sync_with_stdio(0);
#define INF 1e9
using namespace std;
typedef pair<int, int> pint;
typedef pair<int, pair<int, int>> ppint;

vector<pint> edges[4009];
priority_queue<pint, vector<pint>, greater<pint>> pq;
priority_queue<ppint, vector<ppint>, greater<ppint>> pq2;
int dist[4009];      // for fox
int dist2[4009][2];  // for wolf

int main() {
    init;
    int N, M;
    cin >> N >> M;

    // input edges
    int a, b, d;
    for (int i = 0; i < M; i++) {
        cin >> a >> b >> d;
        edges[a].push_back({d * 2, b});
        edges[b].push_back({d * 2, a});
    }

    // dijkstra (fox)
    fill(dist, dist + N + 1, INF);
    dist[1] = 0;
    pq.push({0, 1});

    while (pq.size()) {
        auto [curd, cur] = pq.top();
        pq.pop();
        if (dist[cur] < curd) continue;
        for (int i = 0; i < edges[cur].size(); i++) {
            auto [nxtd, nxt] = edges[cur][i];
            if (dist[nxt] > curd + nxtd) {
                dist[nxt] = curd + nxtd;
                pq.push({dist[nxt], nxt});
            }
        }
    }

    // dijkstra (wolf)
    // dist2[i][0] -> even step's dist (next step 1/2) / dist2[i][1] -> odd step's dist (next step *2)
    for (int i = 1; i < N + 2; i++) {
        dist2[i][0] = INF;
        dist2[i][1] = INF;
    }
    dist2[1][0] = 0;

    pq2.push({0, {1, 0}});
    while (pq2.size()) {
        int curd = pq2.top().first;
        int cur = pq2.top().second.first;
        int step = pq2.top().second.second;
        pq2.pop();
        if (step % 2 == 0) {
            if (dist2[cur][0] < curd) continue;
        } else {
            if (dist2[cur][1] < curd) continue;
        }
        for (int i = 0; i < edges[cur].size(); i++) {
            int nxtd = edges[cur][i].first;
            int nxt = edges[cur][i].second;
            if (step % 2 == 0) {
                nxtd /= 2;
                if (dist2[nxt][1] > curd + nxtd) {
                    dist2[nxt][1] = curd + nxtd;
                    pq2.push({dist2[nxt][1], {nxt, step + 1}});
                }
            } else {
                nxtd *= 2;
                if (dist2[nxt][0] > curd + nxtd) {
                    dist2[nxt][0] = curd + nxtd;
                    pq2.push({dist2[nxt][0], {nxt, step + 1}});
                }
            }
        }
    }

    int result = 0;
    for (int i = 1; i < N + 1; i++) {
        if (dist[i] < min(dist2[i][0], dist2[i][1])) result++;
    }
    cout << result;
}