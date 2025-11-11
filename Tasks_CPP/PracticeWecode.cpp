#include <iostream>
#include <vector>
using namespace std;

void MergeSort(vector<int> &arr, int l, int r);
void Merge(vector<int> &arr, int l, int m, int r);

int main()
{
    int n;
    cin >> n;
    vector<int> my_array;
    for (int i = 0; i < n; i++)
    {
        string m;
        cin >> m;
        my_array.push_back(long(stoi(m)));
    }

    MergeSort(my_array, 0, n - 1);

    int count = 1;
    for (int i = 0; i < n; i++)
    {
        int diff = my_array[0];
        if (diff != my_array[i])
        {
            count++;
            diff = my_array[i];
        }
    }
    cout << count;
    return 0;
}

void MergeSort(vector<int> &arr, int l, int r)
{
    if (l >= r)
        return;
    int m = l + (r - l) / 2;
    MergeSort(arr, l, m);
    MergeSort(arr, m + 1, r);
    Merge(arr, l, m, r);
}

void Merge(vector<int> &arr, int l, int m, int r)
{
    int n1 = m - l + 1;
    int n2 = r - m;

    vector<int> L(n1), R(n2);

    for (int i = 0; i < n1; i++)
        L[i] = arr[l + i];
    for (int i = 0; i < n2; i++)
        R[i] = arr[m + 1 + i];

    int i = 0, j = 0, k = l;
    while (i < n1 && j < n2)
    {
        if (L[i] <= R[j])
        {
            arr[k] = L[i];
            i++;
        }
        else
        {
            arr[k] = R[j];
            j++;
        }
        k++;
    }

    while (i < n1)
    {
        arr[k] = L[i];
        i++;
        k++;
    }

    while (j < n2)
    {
        arr[k] = R[j];
        j++;
        k++;
    }
}