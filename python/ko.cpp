#include <bits/stdc++.h>
using namespace std;

typedef long long LL;
typedef unsigned long long ull;

const int inf=0x3f3f3f3f;

const int N = 2e5 + 100;

int f[N];

struct Edge
{
    int u,v,w;
    void input()
    {
        scanf("%d%d%d",&u,&v,&w);
    }
    bool operator < (const Edge& a)const{
        return w<a.w;
    }
}edge[N];

int find(int x){
    return x==f[x]?x:f[x]=find(f[x]);
}

bool merge(int x,int y){
    int xx = find(x);
    int yy = find(y);
    if(xx!=yy){
        f[xx] = yy;
        return true;
    }
    return false;
}

void init(int n){
    for (int i = 0; i < n; i++)
    {
        f[i] = i;
    }
    
}

int main()
{   
   int n,m;

   while ( scanf("%d%d",&n,&m)!=EOF && n+m)
   {
    init(n);
    int sum = 0;
        for (int i = 1; i <=m; i++)
        {
            /*code*/
            edge[i].input();
            sum+=edge[i].w;
        }
    sort(edge+1,edge+1+m);
    for (int i = 1; i <=m; i++){
        if(merge(edge[i].u,edge[i].v))
            sum-=edge[i].w;
    }
    printf("%d\n",sum);
    }
    
   }

    return 0;

}