#include <bits/stdc++.h>
using namespace std;
int const N = 10E5+100;

set<int> vetFlag[N];
int parteOriginal[N], parteCorrente[N];
int num1,num2,num3,num4,s,d;
vector<int> vet;
void resolucao(){
    set<int> saindo;
    saindo.insert(num4);

    int flag = -1;
    while(!saindo.empty()){
        flag = *saindo.begin();
        saindo.erase(flag);


        for (auto c : vetFlag[flag]){
            vetFlag[c].erase(flag);
            parteCorrente[c]--;
            if(parteCorrente[c]<=(parteOriginal[c]/2))
                saindo.insert(c);
        }
        vet.push_back(flag);
    }

    if (find(vet.begin(),vet.end(),num3) == vet.end())
        cout<<"stay"<<'\n';
    else{
        cout<<"leave"<<'\n';
    }
}


int main()
{
    cin>>num1>>num2>>num3>>num4;

    for(int i = 0;i<=num1;i++){
        parteOriginal[i]=0;
        parteCorrente[i]=0;
    }

    for (int i = 0; i < num2; i++)
    {
       cin>>s>>d;
       vetFlag[s].insert(d);
       vetFlag[d].insert(s);
       parteOriginal[d]++;
       parteCorrente[d]++;
       parteOriginal[s]++;
       parteCorrente[s]++;

    }
    resolucao();
    

return 0;
}