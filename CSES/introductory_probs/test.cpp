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
	string s;
	cin >> s;
	int tot = s.length();
	if (tot == 1){
		cout << s << endl;
		return;
	}
	unordered_map<char, int> cnt;
	for (int i = 0; i < s.length(); i ++){
		cnt[s[i]] ++;
	}

	//check if valid solution exists, if it is odd, then one number can be odd, if even, everything has to be even
	//
	bool possible = true;
	string out = "";
	if (tot % 2 == 0){
		//everything has to be even
		for (const auto& pair : cnt){
			if (pair.second % 2 != 0){
				cout << "NO SOLUTION" << endl;
				possible = false;
				break;
			}
			for (int rep = 0; rep < pair.second / 2; rep ++){
				out.push_back(pair.first);	
			}

		}
		if (possible){
			for (int loc = out.length() - 1; loc >= 0; loc --){
				 out.push_back(out[loc]);
			}
			cout << out << endl;
		}

	}else{
		//an odd count of one character can be allowed
		//
		char mid_ch = 'a';
		for (const auto& pair : cnt){
			if (pair.second % 2 != 0){
				if (mid_ch == 'a'){
					mid_ch = pair.first;
				}else{
					cout << "NO SOLUTION" << endl;
					possible = false;
					break;
				}
			}
			for (int rep = 0; rep < pair.second / 2; rep ++){
				out.push_back(pair.first);	
			}

		}
		
		if (possible){
			for (int loc = out.length() - 1; loc >= 0; loc --){
				if (loc == out.length() - 1 && mid_ch != 'a'){
					out.push_back(mid_ch);
				}
				 out.push_back(out[loc]);
			}
			cout << out << endl;
		}


	}
	return;
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

