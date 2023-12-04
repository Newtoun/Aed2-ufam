#include <bits/stdc++.h>
using namespace std;


int main(){
   int long long num1,num2,num3;
   int long long indice = 0,flag = 0;

   cin>> num1 >>num2>>num3;

   vector<long long> pessoa(num1);
   vector<long long> casa(num2);

   for(int i = 0;i<num1;i++){
    cin >> pessoa[i];
   }

   for(int i = 0;i<num2;i++ ){
    cin >> casa[i];
   }

   sort(pessoa.begin(), pessoa.end());
   sort(casa.begin(), casa.end());

   for (int i = 0; i < num1; i++)
   {
   
    while(indice<num2)
    {

        if(casa[indice] + num3 < pessoa[i])
        {  
        indice++;

        }
        else if( casa[indice]-num3 > pessoa[i]){
            break;
        }
        else{
            indice++;
            flag++;
            break;
        }

    }


   }


   cout << flag << endl;

}