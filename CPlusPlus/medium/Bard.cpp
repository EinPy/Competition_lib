#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

void solve(int N,int E, vector<set<int> > arr) {
    //check all days, if the bard appears, reset those who know
    //cout <<"start"<<endl;
    vector<set<int> > knowsong;

    for (int i = 0; i < E; i ++){
        //check if bard is in night
        if (arr[i].count(1) > 0){
            set<int> newsong;
            for (auto x : arr[i]){
                newsong.insert(x);
            }
            knowsong.push_back(newsong);
        }else{
            for (int j = 0; j < knowsong.size(); j++){
                bool someone_knows = false;
                for (auto x : arr[i]){
                    if (knowsong[j].count(x) > 0){
                        someone_knows = true;
                    }
                }
                if (someone_knows){
                    //everybody now knows
                    for (auto x: arr[i]){
                        knowsong[j].insert(x);
                    }
                }
            }
        }
    }
    set<int>  know_all;
    know_all.insert(1);
    for (int i = 2; i <= N; i++){
        bool in_all = true;
        if (knowsong.size() == 0){
            in_all = false;
        }
        for (int j = 0; j< knowsong.size(); j++){
            if (knowsong[j].count(i) == 0){
                in_all = false;
            }
        }
        if (in_all){
            know_all.insert(i);
        }
    }
    for (auto x : know_all){
        cout << x << endl;
    }
}


int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    int N, E;
    cin >> N;
    cin >> E;
    int a, b;
    vector<set<int> > arr;
    for (int i = 0; i < E; i++){
        cin >> a;
        set<int> day;
        for (int j = 0; j<a; j++){
            cin >> b;
            day.insert(b);
        }
        arr.push_back(day);
    }
    solve(N, E, arr);
}