#include <bits/stdc++.h>
using namespace std;
const int N = 2e5 + 7;
int a[N];
int b[N];
vector<int> vet[N];
queue<int> qq;
bool vis[N];

int main(){
    int c,p,x,l,i,y,flag=0;
    int u,v;
    cin>>c>>p>>x>>l;

    for(i=0;i<p;i++){
        scanf("%lld %lld", &u,&v);
        vet[u].push_back(v);
        vet[v].push_back(u);
        a[u]++;
        a[v]++;
        b[u] = a[u];
        b[v] = a[v];
    }

    qq.push(l);

    while(!qq.empty()){
        y = qq.front();
        qq.pop();
        if(vis[y])
            continue;
        
        else{
            vis[y] = 1;
        }

        if(y==x){
            flag=1;
            break;
        }

        for(int xx:vet[y]){
            if(a[xx]==0)
                continue;
            a[xx]--;
            if(a[xx]<=b[xx]/2){
                qq.push(xx);
            }
        }
    }

    if (flag){
        cout<<"stay\n";
    }
    else{
        cout<<"leave\n";
    }

    return 0;
}