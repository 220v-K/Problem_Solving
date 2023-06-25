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

string rev(string s){
    reverse(s.begin(), s.end());
    return s;
}
string tail(string s){
    return s.substr(1,s.size());
}
string supper(string s){
    return s.substr(0,(int)ceil((double)s.size()/3.0));
}
bool caseFunction(string s){
    string str=s;
    if(str==supper(s)+rev(supper(s))+supper(s)
       ||str == supper(s)+tail(rev(supper(s)))+supper(s)
       ||str == supper(s)+rev(supper(s))+tail(supper(s))
       ||str == supper(s)+tail(rev(supper(s)))+tail(supper(s))
       )
        return true;
    return false;
}

int T;
int main() {
    init;
    cin>>T;
    while(T--){
        string tmp;
        cin>>tmp;
        
        if(caseFunction(tmp)){
            cout<<1<<"\n";
        }else{
            cout<<0<<"\n";
        }
    }
    
    return 0;
}