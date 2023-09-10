#include <stdlib.h>
#include <string.h>
#include <stdio.h>

long long pow_ll(long long n, int exp);
int is_palindrome(char *s);
void mirror(char *s, int with_middle);
int str_all(char *s, char ch);

// Input: 1 <= left.length, right.length <= 18
int superpalindromesInRange(char *left, char *right)
{

    const long long l_int = atoll(left);
    const long long r_int = atoll(right);

    // It is our main iterator. On each iteration we will mirror it's string representation
    // and compute half^2. We should carefully handle cases when half is about to increase
    // it's length (when 9999 becomes 10000). We are computing first value of half to be
    // as near as possible to left.
    // Note: half >= 0 and half.digits <= 5
    long long half = pow_ll(10, (int)(strlen(left) / 2 / 2)) - 1;

    char s[19];               // main array for storing various string representations
    sprintf(s, "%lld", half); // we need before loop this to compute with_middle
    int with_middle = strlen(s) % 2 != 0; // used in mirror function
    int found = 0; // result of function
    for (;;)
    {
        sprintf(s, "%lld", half);
        // will len increase at next iteration?
        const int len_increase = str_all(s, '9');
        mirror(s, with_middle);

        // n is a palindrome
        long long n = atoll(s);
        long long n_pow = n * n;

        // carefully incrementing half for next iteration
        ++half;
        if (len_increase)
        {
            if (with_middle)
            {
                half /= 10;
            }
            with_middle = !with_middle;
        }

        // various checks
        if (n_pow < l_int || !is_palindrome(s))
            continue;
        if (n_pow > r_int)
            break;

        sprintf(s, "%lld", n_pow);
        if (is_palindrome(s))
        {
            found++;
        }
    }

    return found;
}

int str_all(char *s, char ch)
{
    for (int i = 0; i < strlen(s); i++)
    {
        if (s[i] != ch)
            return 0;
    }
    return 1;
}

long long pow_ll(long long n, int exp)
{
    long long res = 1;
    for (int j = 0; j < exp; j++)
    {
        res *= n;
    }
    return res;
}

int is_palindrome(char *s)
{
    int i = 0;
    int j = strlen(s) - 1;
    while (i < j)
    {
        if (s[i] != s[j])
            return 0;
        i++;
        j--;
    }
    return 1;
}

// s must be long enought to hold mirrored input with null character at the end
void mirror(char *s, int with_middle)
{
    const int len = strlen(s);
    const int limit = len - (with_middle ? 1 : 0);
    const int new_len = len * 2 - (with_middle ? 1 : 0);

    for (int i = 0; i < limit; i++)
    {
        int j = new_len - i - 1;
        s[j] = s[i];
    }
    s[new_len] = '\0';
}