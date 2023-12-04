#include <bits/stdc++.h>
using namespace std;

int main()
{
ios_base::sync_with_stdio(false);
cin.tie(NULL);
cout.tie(NULL);

long long num1,num2,i;

cin>>num1>>num2;
vector<long long> vet[num1+1];
vector<long long> con(num1+1,1);

for(i=0;i<num2;i++)
{
    long long num3,num4;
    cin>>num3>>num4;
    vet[num3].push_back(num4);
    vet[num4].push_back(num3);

}

queue<long long> q;
q.push(1);
vector<bool> vis(num1+1,false);
vis[1]=true;

while(!q.empty()){
    long long b=q.front();
    q.pop();
    con[b]=0;
    for(auto c: vet[b]){
        if(!vis[c]){
            q.push(c);
            vis[c]=true;
        }
    }
}

long long flag=1;

for(i=1;i<=num1;i++){   
    if(con[i]) {cout<<i<<'\n';flag=0;}
}
if(flag)
{ 
    cout<<"Connected"<<'\n';
}

return 0;
}