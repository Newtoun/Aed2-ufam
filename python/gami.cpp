#include <iostream>
using namespace std;

void espiral(int linha,int coluna,int resultado_x,int resultado_y,int nivel,int num){

    if(linha == resultado_x && coluna==resultado_y){
        printf("%d\n",num);
    }

    if (nivel%2==0){
        if(coluna<nivel+1){
            return espiral(linha,coluna+1,resultado_x,resultado_y,nivel,num-1);
        }
        if(coluna==nivel+1){
            return espiral(linha-1,coluna,resultado_x,resultado_y,nivel,num-1);
        }

    }
    else{
        if (linha<nivel+1){
            return espiral(linha+1,coluna,resultado_x,resultado_y,nivel,num-1);
        }

        if (linha == nivel+1){
            return espiral(linha,coluna-1,resultado_x,resultado_y,nivel,num-1);
        }

    }

}

int main(){
    int linha,coluna;

    int repeticao;
    cin>>repeticao;

    while(repeticao>0){
        cin>>linha>>coluna;

        if (linha>coluna){
        espiral(linha,1,linha,coluna,linha,linha*linha);

        }else{
        espiral(1,coluna,linha,coluna,coluna,coluna*coluna);
        }

        repeticao--;
    }
    
    return 0;
}

