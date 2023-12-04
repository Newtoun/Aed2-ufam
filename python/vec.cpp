#include<bits/stdc++.h>
using namespace std;
#define MOD 1000000007
#define MOD1 998244353
#define INF 1e18
#define nline "\n"
#define pb push_back
#define ppb pop_back
#define mp make_pair
#define ff first
#define ss second
#define PI 3.141592653589793238462
#define set_bits __builtin_popcountll
#define sz(x) ((int)(x).size())
#define all(x) (x).begin(), (x).end()
#define vi vector<int>
#define vll vector<long long>
#define si set<int>
#define ump unordered_map<int,int>
#define yes cout<<"YES"<<nline
#define no cout<<"NO"<<nline
 
typedef long long ll;
typedef unsigned long long ull;
typedef long double lld;
 
#ifndef ONLINE_JUDGE
#define debug(x) cerr << #x <<" "; _print(x); cerr << endl;
#else
#define debug(x)
#endif
 
void _print(ll t) {cerr << t;}
void _print(int t) {cerr << t;}
void _print(string t) {cerr << t;}
void _print(char t) {cerr << t;}
void _print(lld t) {cerr << t;}
void _print(double t) {cerr << t;}
void _print(ull t) {cerr << t;}
 
template <class T, class V> void _print(pair <T, V> p);
template <class T> void _print(vector <T> v);
template <class T> void _print(set <T> v);
template <class T, class V> void _print(map <T, V> v);
template <class T> void _print(multiset <T> v);
template <class T, class V> void _print(pair <T, V> p) {cerr << "{"; _print(p.ff); cerr << ","; _print(p.ss); cerr << "}";}
template <class T> void _print(vector <T> v) {cerr << "[ "; for (T i : v) {_print(i); cerr << " ";} cerr << "]";}
template <class T> void _print(set <T> v) {cerr << "[ "; for (T i : v) {_print(i); cerr << " ";} cerr << "]";}
template <class T> void _print(multiset <T> v) {cerr << "[ "; for (T i : v) {_print(i); cerr << " ";} cerr << "]";}
template <class T, class V> void _print(map <T, V> v) {cerr << "[ "; for (auto i : v) {_print(i); cerr << " ";} cerr << "]";}
 
// code by SHUBHAM
 
int main()
{
#ifndef ONLINE_JUDGE
	freopen("Error.txt", "w", stderr);
#endif
	int t=1; 
	while(t--)
	{
		ll n; cin >> n;
		vll v1(n),v2(n);
		for (int i = 0; i < n; ++i)
		{
			cin >> v1[i];
		}
		for (int i = 0; i < n; ++i)
		{
			cin >> v2[i];
		}
		ll dp[2][n+1];
 
		dp[0][0] = 0;
		for (int i = 0; i < 2; ++i)
		{
			for (int j = 0; j <= n; ++j)
			{
				dp[i][j] = 0;
			}
		}
		for (int i = 1; i <= n; ++i)
		{
			dp[0][i] = max(dp[0][i-1],dp[1][i-1]+v1[i-1]);
			dp[1][i] = max(dp[1][i-1],dp[0][i-1]+v2[i-1]);
		}
 
		cout<<max(dp[0][n],dp[1][n])<<nline;
	}
}