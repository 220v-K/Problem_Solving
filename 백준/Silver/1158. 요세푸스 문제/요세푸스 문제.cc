#include <iostream>
#include <queue>
using namespace std;

int main()
{
	queue<int> Q;
	int N, K;
	cin >> N >> K;
	
	for (int i = 0; i < N; i++)
	{
		Q.push(i + 1);
	}

	cout << '<';
	int temp;
	while (Q.size() != 1)
	{
		//K-1회 pop 후 push
		for (int i = 0; i < K - 1; i++)
		{
			temp = Q.front();
			Q.pop(); Q.push(temp);
		}
		//그 이후 pop
		cout << Q.front() << ", ";
		Q.pop();
	}
	cout << Q.front() << '>';
}