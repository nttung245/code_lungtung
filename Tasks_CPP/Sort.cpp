#include <iostream>
#include <vector>

using namespace std;

void Selection_sort(vector<int> &array)
{
    int n = array.size();
    int a = 0;
    int b = 0;
    for (int i = 0; i < n - 1; i++)
    {
        int min = i;
        for (int j = i + 1; j < n; j++)
        {
            if (array[j] < array[min])
            {
                min = j;
                a++;
            }
        }
        int temp = array[i];
        array[i] = array[min];
        array[min] = temp;

        if (a != b)
        {
            for (int k = 0; k < n; k++)
            {
                cout << array[k] << " ";
            }
            cout << '\n';
            b = a;
        }
    }
}

int main()
{
    int n;
    cin >> n;
    vector<int> my_array;
    for (int i = 0; i < n; i++)
    {
        int m;
        cin >> m;
        my_array.push_back(m);
    }
    Selection_sort(my_array);
    return 0;
}