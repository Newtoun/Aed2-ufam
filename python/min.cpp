#include <bits/stdc++.h>
using namespace std;

#define N 101
#define INF 999999

static int grafo[N][N];

int main()
{   
    int casos = 0;
    int u,v;

    while (scanf("%d%d", &u,&v) && ( u || v) )
    {
        set <int> vec;

        for (int i = 0; i < N; ++i)
        {
            for (int j = 0; j < N; ++j)
            {
                grafo[i][j] = INF;
            }
        }

        for (int i = 0; i < N; ++i)
        {
            grafo[i][i] = 0;
        }

        grafo[u-1][v-1] = 1;
        vec.insert(u);
        vec.insert(v);

        
        while( scanf("%d%d",&u,&v) && (u||v)){
            grafo[u-1][v-1] = 1;
            vec.insert(u);
            vec.insert(v);
        }

        for( int  k = 0;k<N;++k){
            for(int  i = 0;i<N;++i){
                for(int  j = 0;j<N;++j){
                    if ( grafo[i][j]>grafo[i][k] + grafo[k][j]){
                        grafo[i][j] = grafo[i][k] + grafo[k][j];
                    }
                }
            }
        }

        int soma = 0;
        for (int i = 0; i < N; ++i)
        {
            for (int j = 0; j < N; ++j){
                if(i!=j && grafo[i][j] != INF){
                    soma = soma + grafo[i][j];
                }
            }
        }
        
        int setSize = vec.size();
        printf("Case %d: average length between pages = %.3f clicks\n",casos++,(float) soma /(setSize * (setSize - 1)) );

    }
    return 0;

}