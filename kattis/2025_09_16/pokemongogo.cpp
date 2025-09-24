#include <bits/stdc++.h>

using namespace std;


#define ll long long
#define ld long double
#define sza(x) ((int)x.size())
#define all(a) (a).begin(), (a).end()

const int MAX_N = 1e5 + 5;
const ll MOD = 1e9 + 7;
const ll INF = 1e9;
const ld EPS = 1e-9;


void setup(vector<vector<int>> & m, vector<vector<int>> & dp, int & start, int & N)
{
    for (int i = 0; i <N; i++)
    {
        if (i != start)
        {
            //the path that ends at i and has visited the set of start and i
            dp[i][1 << start | 1 << i] = m[start][i];
        }
    }
}


void solve (vector<vector<int>> & m, vector<vector<int>> & dp, int & start, int & N)
{
    for (int r = 3; r <= N; r++)
    {
        //iterate over all bit sets of size N with r bits set to 1, how do I do that?
        //cannot just do nested for loops
        //for subset in combinations(r, N);
        //use gospoers hack
        
        int set = (1 << r) - 1; //left shif 1 by the number of ones and subrtact 1. 1 << 3 = 1000 (8) 8 - 1 = 7 (0111)
        int limit = (1 << N);
        while (set < limit)
        {
            //cannot have a path that does not include the starting node
            if (set & start == 0)
            {
                continue;
            }
            for (int next = 0; next < N; next ++)
            {
                //the node that was added cannot be the start node, and it also has to be one of the nodes that
                //are set to 1 in the current subset
                if (next == start || (set & (1 << next) == 0))
                {
                    continue;
                }
                // the subset without the next node
                int state = set ^ (1 << next);
                int mindist = INF;
                // is this note where I add the current node no?
                for (int prev_end = 0; prev_end < N; prev_end++)
                {
                    if (prev_end == start || prev_end == next || set & (1 << prev_end) == 0)
                    {
                        continue;
                    }
                    //check the distance from the previous end to this one
                    int newdist = dp[prev_end][state] + m[prev_end][next];
                    if (newdist < mindist)
                    {
                        mindist = newdist;
                        dp[next][set] = mindist;
                    }
                }
            }
            //the actual gospers hack
            int c = set & - set;
            int r = set + c;
            set = (((r ^ set) >> 2) / c) | r;
        }
    }
}

int min_cost(vector<vector<int>> m, vector<vector<int>> dp, int start, int N)
{
    int end_state = (1 << N) - 1;
    int min_cost = INF;
    for (int e = 0; e < N; e++)
    {
        if (e == start)
        {
            continue;
        }
        int cost = dp[e][end_state] + m[e][start];
        if (cost < min_cost)
        {
            min_cost = cost;
        }
    }

    return min_cost;

}
void tsp (vector<vector<int>> m, int start, int N)
{
    vector<int> row(N, INF);
    vector<vector<int>> dp(N, row);
    setup(m, dp, start, N);
    solve(m, dp, start, N);
    //minCost = findMinCost(m, memo, S, N);
    //tour = findOptimalTour(m, memo, S, N);

}


void solve() {
    //Traveling salesman problem,
    //and dp? find shortest route that return sto start in grid that also includes
    //all pokemon in a list
    //2d grid structure
    //
    int N;
    cin >> N;
    vector<int> row(N, -1);
    vector<vector<int>> graph(N, row);
    int cur_pok = 0;
    unordered_map<string, int> name_to_num;
    unordered_map<int, string> num_to_name;

    

    for (int i = 0; i < N; i ++)
    {
        int a, b;
        string c;
        cin >> a >> b >> c;
        
    }
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    int tc = 1;
    // cin >> tc;
    for (int t = 1; t <= tc; t++) {
        // cout << "Case #" << t << ": ";
        solve();
    }
}

