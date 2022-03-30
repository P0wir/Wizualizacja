#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void foo(int n, int tab[])
{
    for (int i=0; i<n; i++)
    {
        tab[i]=abs(tab[i]);
    }
}

int main()
{
    int tablica[4]={3,-4,55,-11};
    foo(4,tablica);
    for(int i=0; i<4; i++)
    {
                printf("[%d]=%d\n", i, tablica[i]);
    }
}
