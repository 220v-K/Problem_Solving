#include <algorithm>
#include <iostream>
#include <queue>
#include <vector>

#define init cin.tie(0)->ios_base::sync_with_stdio(0);
#define INF 1e9
using namespace std;
typedef pair<int, int> pint;

vector<vector<int>> answer;

int main() {
    init;
    int T;
    cin >> T;

    for (int p = 0; p < T; p++) {
        vector<pint> edges[2009];
        priority_queue<pint, vector<pint>, greater<pint>> pq;
        int dist[2009];

        int n, m, t;
        cin >> n >> m >> t;
        int s, g, h;
        cin >> s >> g >> h;

        int a, b, d;
        for (int i = 0; i < m; i++) {
            cin >> a >> b >> d;
            edges[a].push_back({d, b});
            edges[b].push_back({d, a});
        }

        int tList[101], x;
        for (int i = 0; i < t; i++) {
            cin >> x;
            tList[i] = x;
        }

        fill(dist, dist + n + 1, INF);
        dist[s] = 0;
        pq.push({0, s});

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

        // g, h중 더 가까운 것의 거리를 저장
        int distA;
        int s2;
        if (dist[g] < dist[h]) {
            distA = dist[g];
            s2 = h;
        } else {
            distA = dist[h];
            s2 = g;
        }
        // g - h 사이의 거리
        int distB;
        for (int i = 0; i < edges[g].size(); i++) {
            if (edges[g][i].second == h) {
                distB = edges[g][i].first;
                break;
            }
        }
        // (s2) - (목적지) 의 최단거리
        int distC[2009];
        fill(distC, distC + n + 1, INF);
        distC[s2] = 0;
        pq.push({0, s2});

        while (pq.size()) {
            auto [curd, cur] = pq.top();
            pq.pop();
            if (distC[cur] < curd) continue;
            for (int i = 0; i < edges[cur].size(); i++) {
                auto [nxtd, nxt] = edges[cur][i];
                if (distC[nxt] > curd + nxtd) {
                    distC[nxt] = curd + nxtd;
                    pq.push({distC[nxt], nxt});
                }
            }
        }

        /* s - (g or h) / g - h / s2(g or h) - 목적지 의 세 거리의 합이
        s - 목적지 의 거리와 동일하면 g-h를 지나는 최단 경로가 존재하는 것. */
        vector<int> result;
        for (int i = 0; i < t; i++) {
            int goal = tList[i];
            if (distA + distB + distC[goal] == dist[goal]) {
                result.push_back(tList[i]);
            }
        }

        sort(result.begin(), result.end());
        answer.push_back(result);
    }

    for (int p = 0; p < T; p++) {
        for (int i = 0; i < answer[p].size(); i++) {
            cout << answer[p][i];
            if (i != answer[p].size() - 1) {
                cout << " ";
            }
        }
        if (p != T - 1) {
            cout << "\n";
        }
    }
}