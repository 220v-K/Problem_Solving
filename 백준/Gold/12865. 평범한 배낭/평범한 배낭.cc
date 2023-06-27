#include <string.h>

#include <iostream>
using namespace std;

int N, K, W[101] = {
              0,
},
          V[101] = {
              0,
};
int dp[101][100001] = {
    0,
};

int Max(int a, int b) {
    if (a > b)
        return a;
    else
        return b;
}

int knapsack(int W[], int V[], int num, int capacity) {
    if (num == N)
        return 0;
    //이미 계산했던 값이면 그대로 return, 아니라면 계산 (Dynamic Programming)
    if (dp[num][capacity] != 0)
        return dp[num][capacity];
    else {
        int value_insert = 0, value_not = 0;
        //배낭에 넣을 수 있을 때(현재 capacity + 더한 무게가 최대 버틸 수 있는 무게보다 작을 때)
        if (capacity + W[num] <= K) {
            value_insert = knapsack(W, V, num + 1, capacity + W[num]) + V[num];
        }
        value_not = knapsack(W, V, num + 1, capacity);

        dp[num][capacity] = Max(value_insert, value_not);
        //둘 중 큰 값을 return
        return dp[num][capacity];
    }
}

int main() {
    cin >> N >> K;

    for (int i = 0; i < N; i++) {
        cin >> W[i] >> V[i];
    }
    cout << knapsack(W, V, 0, 0);
}