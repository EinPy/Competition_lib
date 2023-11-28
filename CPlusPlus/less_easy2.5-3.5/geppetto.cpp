#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

const int MAXN = 21;
int N, M;
bool used[MAXN];
vector<int> adj[MAXN];


// pretty print
void pp(){
    cout << "currently on pizza" << endl;
    for (auto x : used){
        cout << x << " ";
    }
    cout << endl;
}

//immediatly start by going down to deepest node
//use it, go up one step
// when up one step, if that node was not ok, we go up again
//if that node was ok, subnodes can be checked with this node included as well
//that will add an equal amount of sets
// this will all bubbel up recursively. 
//wow, this is a super super smart solution. 

int solve(int x) {
    cout << "checking " << x << endl;
    pp();
    if (x == N){
        return 1; //all nodes have been considered, this is a valid subset
    }
    //count number of permutations that can be formed with items x+1 to n
    int rest = solve(x + 1); 
    bool ok = true;
    for (auto v : adj[x]){
        if(used[v]){
            ok = false;
        }
    }
    //if none of the currently used edges, were disallowed
    if (ok){
        used[x] = 1;
        rest += solve(x+1);
        used[x] = 0;
    }
    return rest;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    cin >> N >> M;
    //for each pizza check how many ingredients it can be paired with. 
    int a, b;
    for (int i = 0; i<M;i++){
        cin >> a >>b;
        a --;
        b --;
        adj[a].push_back(b);
        adj[b].push_back(a);
    }
    // can always make empty pizza
    cout << solve(0) << endl;
}