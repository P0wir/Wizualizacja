#include <stdio.h>
#include <stdlib.h>

void foo(int n, int tab[])
{
    for (int i=0; i<n; i++)
    {
        tab[i]=0;
    }
}

int main()
{
    int tablica[4];
    foo(4,tablica);
    for(int i=0; i<4; i++)
    {printf("[%d]=%d\n", i, tablica[i]);
    }
}
