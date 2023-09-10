#include <string.h>
#include <stdio.h>

int is_palindrome(const char *s);
void mirror(char *s, int with_middle);

int superpalindromesInRange(char *left, char *right)
{
    const long long l_int, r_int;
    sscanf(left, "%lld", &l_int);
    sscanf(right, "%lld", &r_int);

    int found = 0;
    char s[20];
    for (int with_middle = 0; with_middle <= 1; with_middle++)
        for (int i = 1; i <= 99999; i++)
        {
            {
                if (i >= 9999 && !with_middle)
                    break;

                sprintf(s, "%d", i);
                mirror(s, with_middle);
                if (is_palindrome(s))
                {
                    long long n;
                    sscanf(s, "%lld", &n);

                    n *= n;
                    if (n < l_int)
                        continue;
                    if (n > r_int)
                        break;

                    sprintf(s, "%lld", n);
                    if (is_palindrome(s))
                        found++;
                }
            }
        }

    return found;
}

int is_palindrome(const char *s)
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