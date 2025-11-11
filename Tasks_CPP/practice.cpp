#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

class Solution
{
public:
    char nextGreatestLetter(vector<char> &letters, char target)
    {
        int start = 0;
        int end = letters.size() - 1;
        int smallest_letter = letters[0];
        while (start <= end)
        {
            int mid = floor((start + end) / 2);
            if ((int)letters[mid] > (int)target)
            {
                smallest_letter = letters[mid];
                end = mid - 1;
            }
            else
            {
                start = mid + 1;
            }
        }

        return smallest_letter;
    }
};