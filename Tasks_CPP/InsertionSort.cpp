#include <iostream>
#include <string>
#include <stdexcept>
#include <cstdlib>
#include <vector>

using namespace std;

void Insertion(vector<int> array)
{
    int n = array.size();
    for (int i = 1; i < n; i++)
    {
        int current = array[i];
        int j = i - 1;
        while (array[j] > current && j >= 0)
        {
            array[j + 1] = array[j];
            j--;
        }
        array[j + 1] = current;
    }
}

int main()
{
    int n;
    cin >> n;
    vector<int> my_array;
    for (int i = 0; i < n; i++)
    {
        string m;
        cin >> m;
        my_array.push_back(stoi(m));
    }
    Insertion(my_array);
    int diff = my_array[0];
    int count = 1;
    for (int i = 0; i < n; i++)
    {
        if (diff != my_array[i])
        {
            count++;
            diff = my_array[i];
        }
    }
    cout << count;
    return 0;
}
