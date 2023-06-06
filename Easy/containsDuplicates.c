#include "stdio.h"
#include <stdbool.h>

bool containsDuplicate(int* nums, int numsSize){
    // i = 0, 1, 2, 3, .... numsSize - 1
    for(int i = 0; i < numsSize - 1; i++) {  
    // j = 1, 2, 3, .... numsSize
        for (int j = i + 1; j < numsSize; j++) {
            if (nums[i] == nums[j]) {
                return true;
            }
        } 
    }
    return false;
}