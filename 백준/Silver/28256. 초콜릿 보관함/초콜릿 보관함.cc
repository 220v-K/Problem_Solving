#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <stack>
#include <cstring>
#include <cmath>
#include <tuple>
#include <map>
#include <iomanip>
#include <numeric>
#define init cin.tie(0)->ios_base::sync_with_stdio(0);

using namespace std;

typedef long long ll;
typedef pair<int,int> pint;
typedef tuple<int,int,int> iii;
typedef pair<ll, ll> pll;

int T,n;
vector<int>v;

char maps[3][3];
int visited[3][3];
int dx[4]={0,0,1,-1};
int dy[4]={1,-1,0,0};
vector<int>res;
int cnt;
void dfs(int x, int y){
    visited[x][y]=1;
    for(int i=0;i<4;i++){
        int xx=x+dx[i];
        int yy=y+dy[i];
        if(xx==1&&yy==1)continue;
        if(xx>=0&&xx<3&&yy>=0&&yy<3&&visited[xx][yy]==0&&maps[xx][yy]=='O'){
            cnt++;
            dfs(xx, yy);
        }
    }
}


int main() {
    init;
    cin>>T;
    while(T--){
        v.clear();
        res.clear();
        cnt=0;
        
        for(int i=0;i<3;i++){
            for(int j=0;j<3;j++){
                cin>>maps[i][j];
                visited[i][j]=0;
            }
        }
        cin>>n;
        for(int i=0;i<n;i++){
            int tmp;
            cin>>tmp;
            v.push_back(tmp);
        }
        
        
        // output -> 화면의 표시가 올바르면 1 but 0
        // 초콜릿이 들어있는 :연결된: 칸의 개수
        // 숫자 여러개면 오름차순으로 표시됨
        for(int i=0;i<3;i++){
            for(int j=0;j<3;j++){
                if(visited[i][j]==0&&maps[i][j]=='O'){
                    cnt++;
                    dfs(i, j);
                    res.push_back(cnt);
                    cnt=0;
                }
            }
        }
        
        
        sort(res.begin(),res.end());

        if(res.size()!=v.size()){
            cout<<0<<"\n";
        }else{
            bool chk = false;
            for(int i=0;i<res.size();i++){
                if(res[i]!=v[i])
                    chk=true;
            }
            if(chk)cout<<0<<"\n";
            else{
                cout<<1<<"\n";
            }
        }
        
    }
    return 0;
}