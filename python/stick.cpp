#include <bits/stdc++.h>
using namespace std;

int main(){
    int tam;
    long long media,flag;
    cin>>tam;
    vector<int> vet(tam);

    for(int i=0;i<tam;i++){
        cin>>vet[i];
    }

    sort(vet.begin(),vet.end());

    media = vet[tam/2];

    for(int i=0;i<tam;i++){
       flag+=abs(media-vet[i]);
    }

    cout<<flag<<endl;


    return 0;
}