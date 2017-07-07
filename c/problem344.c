#include "leetcode.h"
char* reverseString(char* s) {
    size_t size = strlen(s);
    char *rev = (char*)calloc(size + 1, sizeof(char));
    for(int i = 0; i < size; ++i)
    {
        rev[i] = s[size - 1 - i];
    }
    return rev;
}

void test()
{
    char *s = "hello";
    s = reverseString(s);
    printf("%s\n", s);
    free(s);
}