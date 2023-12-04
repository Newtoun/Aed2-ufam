#include <bits/stdc++.h>
using namespace std;

int main()
{

long long int n,vet1[100002],vet2[100002],x;

cin>>n;

memset(vet1,0,100002);

for(int i=1;i<=n;i++){
    cin>>x;
    vet1[x]++;
}

vet2[0]=0;
vet2[1] = vet1[1];

for(int i=2;i<=100001;i++){
    vet2[i] = max(vet2[i-1],vet2[i-2]+i*vet1[i]);
}

cout<<vet2[100001];
    
return 0;
}