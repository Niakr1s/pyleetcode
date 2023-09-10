#include "n906_super_palindromes.h"
#include <assert.h>
#include <stdio.h>

int main()
{
    struct test_case
    {
        char left[20];
        char right[20];
        int expected;
    };

#define LEN 4
    struct test_case tests[LEN] = {
        {"40000000000000000", "50000000000000000", 2},
        {"4", "1000", 4},
        {"1", "11111", 6},
        {"1", "2", 1},
    };

    int errors[LEN];
    int errors_count = 0;

    for (int i = 0; i < LEN; i++)
    {
        struct test_case *test = &tests[i];
        int got = superpalindromesInRange(test->left, test->right);
        int ok = got == test->expected;
        errors[i] = !ok;
        if (!ok)
            errors_count++;

        printf("[%4s] [TEST #%d] left: %s, right: %s, got: %d, expected: %d\n",
               ok ? "OK" : "FAIL", i, test->left, test->right, got, test->expected);
    }
    return errors_count;
}