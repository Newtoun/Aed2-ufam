#include <bits/stdc++.h>
using namespace std;

int main(){
    int num;
    long long flag=0;
    string word;
    cin>>word;
	cin>>num;

    int tamanho = word.size();
    word = word+word;

    for(int i = 0,j=0,k=0;i<tamanho;i++){
        while(j+1<2*tamanho && k==0){
            k+=(word[j]=='E');
                j++;
       
        }
        flag+=max(0, num - (j - i - 1));
        k =k-(word[i]=='E');
    }

    cout << flag << endl;
    
}