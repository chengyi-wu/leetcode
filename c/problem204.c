#include "leetcode.h"

int countPrimes(int n) {
    if (n < 2) return 0;
    int* primes = (int*)calloc(n, sizeof(int));
    primes[0] = 1;
    primes[1] = 1;
    int x = sqrt(n);
    for(int i = 2; i < x; ++i)
    {
        if(primes[i] == 0)
        {
            for(int j = i * i; j < n; j += i)
            {
                primes[j] = 1;
            }
        }
    }
    int c = 0;
    for(int i = 10000000; i < n; ++i)
    {
        if(primes[i] == 0)
        {
            ++c;
            printf("%d\n", i);
        }
    }
    free(primes);
    return c;
}

void test()
{
    int n = 100;
    //printf("%d: %d\n", n, countPrimes(n));
    //n = 10000000;
    //printf("%d: %d\n", n, countPrimes(n));
    n = 100000000;
    printf("%d: %d\n", n, countPrimes(n));
}