#include <bits/stdc++.h>
using namespace std;

int main()
{

int tam,num;
cin>>tam;

for(int i=0;i<tam;i++)
{
    cin>>num;
    if (num==1||num==2||num==4||num==5||num==8||num==11)
    {
        cout<<"NO"<<endl;
    }
    else{
        cout<<"YES"<<endl;
    }

}

return 0;
}