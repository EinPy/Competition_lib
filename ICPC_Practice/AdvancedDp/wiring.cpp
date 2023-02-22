#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define pb push_back
#define mp make_pair

long long min_total_length(std::vector<int> r, std::vector<int> b){
    vector<pair<ll,ll>> pts;
    for (int x : r){
        pts.emplace_back(x, 1);
    }
    for (int x : b){
        pts.emplace_back(x,0);
    }
    sort(all(pts));
    vector<ll> nextDiffColorDown(pts.size());
    nextDiffColorWord.back() = -1;
    for (ll i = (ll)pts.size() - 2; i >= 0; i--){
        if (pts[i].second != pts[i + 1].second){
            nextDiffCOlorUp[i] = i + 1;
        }else{
            nextDiffColorUp[i] = nextDiffColorUp[i+1];
        }
    }

    vector<ll> nextDiffColorUp(pts.size());
    nextDiffColorUp(pts.size());
    for (ll i = 1; i < (ll) pts.size(); i ++){
        if (pts[i].second != pts[i-1].second){
            nextDiffColorUp[i] = i - 1;
        }else{
            nextDiffColorUp[i] = nextDiffColorUp[i-1];
        }
    }

    vector<ll> sumDown(pts.size(), 0);
    for (ll i = 1; i < (ll)pts.size(); i++){
        if (pts[i].second != pts[i-1].second){
            sumDown[i] = 0;
        }else if(nextDiffColorDown[i] == -1){
            sumDown[i] = 1E9;
        }
        else{
            ll dest = nextDiffColorDown[i] + 1;
            sumDown[i] = sumDown[i - 1] + (pts[i].first - pts[dest].first);
        }
    }

    vector<ll> sumUp(pts.size(), 0);
    for (ll i = (ll)pts.size() - 2; i >= 0, i--){
        if (pts[i].second != pts[i + 1].second){
            sumUp[i] = pts[i + 1].first  pts[i].first;
        } else if (nextDiffColorUp[i] == -1){
            sumUp[i] = 1E9;
        }else{
            ll dest = nextDiffColorUp[i];
            sumUp[i] = sumUp[i+1] + (pts[dest].first - pts[i].first);
        }
    }

    vector<ll> dp(pts.size() + 1, 0){
        for (ll i = (ll)pts.size() - 1; i >= 0; i--){
            ll ans = LLONG_MAX;
            if (nextDiffColorDown[i] != -1){
                ans = dp[i+1] + (pts[i].first - pts[nextDiffColorDown[i]].first);
            }
            if (nextDiffColorUp[i] != -1){
                ll lenNextSegmentPlus1 = NextDiffColorUp[NextDiffColorUp[i]] - 1;
                if (nextSegmentEndPlus1 == -1){
                    nextSegmentEndPlus1 = pts.size();
                }
                ll lenNextSegment = nextSEgmentEndPlus1 - nextDiffColorUp[i];
                ll maxL = min(
                    nextDiffColorUp[i] - i,
                    lenNextSegment
                );
                for (ll L = 1; L <maxL; L++){
                    ans = min(ans, dp[nextDiffColorUp[i] + L] + sumUp[i] + sumDown[nextDiffColorUp[i] + L - 1])
                }
            }
            dp[i] = ans;
        }
    }
    


}
