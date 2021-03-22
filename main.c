#include <stdio.h>
#include <stdlib.h>

int main()
{
    int sayi;
    printf("sayi gir\n");
    scanf("%d", &sayi);
    int bbasamagi=0;
    int toplam=0;
    while(sayi>0)
    {
        bbasamagi=sayi%10;
        toplam+=bbasamagi;
        sayi=sayi/10;
    }

    printf("girilen sayinin rakamlari toplami : %d" , toplam);


    return 0;
}
