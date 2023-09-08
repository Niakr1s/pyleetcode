#include <uthash.h>

struct entry
{
    int n;
    int idx;
    UT_hash_handle hh;
};

int *twoSum(const int *nums, int numsSize, int target, int *returnSize)
{

    struct entry *hash = NULL;

    for (int i; i < numsSize; i++)
    {
        int needed = target - nums[i];

        struct entry *found;
        HASH_FIND_INT(hash, &needed, found);
        if (found)
        {
            *returnSize = 2;
            int *res = (int *)malloc(*returnSize * sizeof(int));
            res[0] = found->idx;
            res[1] = i;
            return res;
        }

        struct entry *e = malloc(sizeof(struct entry));
        e->n = nums[i];
        e->idx = i;
        HASH_ADD_INT(hash, n, e);
    }

    *returnSize = 0;
    return NULL;
}