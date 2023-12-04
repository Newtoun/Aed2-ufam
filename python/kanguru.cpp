#include <bits/stdc++.h>
using namespace std;

int main(){
    int tam,vet[500005];
    int j=0;

    cin>>tam;
   for(int i=0;i<tam;i++)
		cin>>vet[i];
	 	sort(vet,vet+tam);
	
	for(int i=0;i<tam;i++)
	{
		if(vet[i]>=2*vet[j])
			j++;
	}
	
	cout<<tam-min(j,tam/2)<<endl;
    

    return 0;
    
    
}