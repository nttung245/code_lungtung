#include <iostream>
#include <vector>
using namespace std;

/*void printArrayWithBrackets(const vector<int> &array, int left, int right)
{
    for (int i = 0; i < array.size(); i++)
    {
        if (i == left)
        {
            cout << "[ ";
        }
        cout << array[i] << " ";
        if (i == right)
        {
            cout << "] ";
        }
    }
    cout << endl;
}*/
void merg(vector<int> &array, int left, int mid, int right)
{
    int n1 = mid - left + 1;
    int n2 = right - mid;

    vector<int> L(n1), R(n2);

    for (int i = 0; i < n1; i++)
        L[i] = array[left + i];
    for (int j = 0; j < n2; j++)
        R[j] = array[mid + 1 + j];

    int i = 0, j = 0, k = left;
    while (i < n1 && j < n2)
    {
        if (L[i] <= R[j])
        {
            array[k] = L[i];
            i++;
        }
        else
        {
            array[k] = R[j];
            j++;
        }
        k++;
    }

    while (i < n1)
    {
        array[k] = L[i];
        i++;
        k++;
    }

    while (j < n2)
    {
        array[k] = R[j];
        j++;
        k++;
    }

    // printArrayWithBrackets(array, left, right);
}

void mergsor(vector<int> &array, int left, int right)
{
    if (left >= right)
        return;

    int mid = left + (right - left) / 2;
    mergsor(array, left, mid);
    mergsor(array, mid + 1, right);
    merg(array, left, mid, right);
}

void merg_sor(vector<int> &array)
{
    mergsor(array, 0, array.size() - 1);
}

int main()
{
    int n;
    cin >> n;
    vector<int> array;

    for (int i = 0; i < n; i++)
    {
        long m;
        cin >> m;
        array.push_back(int(m));
    }
    merg_sor(array);

    int count = 1;
    int diff = array[0];
    for (int i = 0; i < array.size(); i++)
    {
        if (diff != array[i])
        {
            count++;
            diff = array[i];
        }
    }
    cout << count;
    return 0;
}
