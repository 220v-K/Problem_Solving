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
    //�̹� ����ߴ� ���̸� �״�� return, �ƴ϶�� ��� (Dynamic Programming)
    if (dp[num][capacity] != 0)
        return dp[num][capacity];
    else {
        int value_insert = 0, value_not = 0;
        //�賶�� ���� �� ���� ��(���� capacity + ���� ���԰� �ִ� ��ƿ �� �ִ� ���Ժ��� ���� ��)
        if (capacity + W[num] <= K) {
            value_insert = knapsack(W, V, num + 1, capacity + W[num]) + V[num];
        }
        value_not = knapsack(W, V, num + 1, capacity);

        dp[num][capacity] = Max(value_insert, value_not);
        //�� �� ū ���� return
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