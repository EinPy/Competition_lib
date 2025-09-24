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



void solve() {
    
    int N; 
    cin >> N;
    unordered_map<string, int> name_to_int;
    int cur = 0;

    vector<pair<int,int>> coords;

    //need one matrix which is the distances from each stop to all others, 
    //the first stop is always at 0, first create a vector of all stops, then convert to matrix
    coords.push_back(make_pair(0,0));
    //need one vector which keeps track of an int which determines which pokemon live at one stop
    vector<int> poks;
    poks.push_back(0);

    for (int i = 0; i<N; i++)
    {
        int a, b;
        string c;
        cin >> a >> b >> c;
        if (name_to_int.find(c) == name_to_int.end())
        {
            name_to_int[c] = cur;
            cur++;
        }
        int cint = name_to_int[c];

        bool found = false;
        for (int j = 0; j < coords.size();j++)
        {   
            int x = coords[j].first;
            int y = coords[j].second;
            if (x == a && y == b)
            {
                poks[j] = poks[j] | (1 << cint);
                found = true;
            }
        }
        if (! found)
        {
            coords.push_back(make_pair(a, b));
            poks.push_back((1 << cint));
        }
    }
    //cout << "coords: " << coords.size() << " poks: " << poks.size() << "\n";
    for ( int i = 0; i < coords.size(); i++)
    {
        //cout << coords[i].first << " " << coords[i].second << " " << poks[i] << "\n";
    }


    vector<int> row(coords.size(), -1);
    vector<vector<int>> grid(coords.size(), row);

    //calculate distance matrix
    for (int i = 0; i < coords.size(); i++)
    {
        for (int j = 0; j < coords.size(); j++)
        {
            grid[i][j] = abs(coords[i].first - coords[j].first) + abs(coords[i].second - coords[j].second);
            grid[j][i] = abs(coords[i].first - coords[j].first) + abs(coords[i].second - coords[j].second);
        }
    }

    //now do subset dp, can be bottom up or top down. since multiple pokemon can be added in each stop, maybe it's
    //easier to do top down??, that is recursively??
    //just thinking if bottom up, int would not be enough to just remove one pokemon, we need to check if possibly multiple 
    //were added, and this can increase a lot? 
    //we have number of locations and number of pokemon
    //
    vector<int> state((1 << cur), INF);
    //then we need ending in each possible location, with each possible set?
    vector<vector<int>> memo(coords.size(), state);
    memo[0][0] = 0;

    int loc = coords.size();
    int pokN = cur;
    //intitial setup
    for (int i = 0; i < loc; i++)
    {
        int st = poks[i];
        memo[i][st] = grid[0][i];
    }

    //check all masks in numerical order
    for (int mask = 0; mask < (1 << pokN); mask++)
    {
        //check if this mask exists for some location
        for (int from = 0; from < loc; from ++)
        {
            if (memo[from][mask] == INF)
            {
                continue;
            }
            //we have some valid value;
            //check what the new mask would become if we go somewhere new
            for (int to = 1; to < loc; to++)
            {
                if (from == to)
                {
                    continue;
                }
                int newmask = mask | poks[to];
                if (newmask != mask)
                {
                    memo[to][newmask] = min(memo[to][newmask], memo[from][mask] + grid[from][to]);
                }
            }
        }
    }
    int FULL = (1 << pokN) - 1;
    int ans = INF;
    for (int i = 1; i < loc;i++)
    {
        ans = min(ans, memo[i][FULL] + grid[i][0]);
    }
    cout << ans;
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

