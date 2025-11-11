#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class ToaDo
{
private:
    int x;
    int y;

public:
    int getX() const { return x; }
    int getY() const { return y; }

    friend istream &operator>>(istream &is, ToaDo &td)
    {
        is >> td.x >> td.y;
        return is;
    }

    friend ostream &operator<<(ostream &os, const ToaDo &td)
    {
        os << td.x << " " << td.y;
        return os;
    }

    ToaDo(int x = 0, int y = 0) : x(x), y(y) {}
};

bool compare(const ToaDo &a, const ToaDo &b)
{
    if (a.getX() != b.getX())
        return a.getX() < b.getX();
    return a.getY() > b.getY();
}

int main()
{
    int n;
    cin >> n;
    vector<ToaDo> my_array(n);

    for (int i = 0; i < n; i++)
    {
        cin >> my_array[i];
    }

    for (int i = 0; i < n - 1; i++)
    {
        for (int j = 0; j < n - i - 1; j++)
        {
            if (my_array[j].getX() > my_array[j + 1].getX())
            {
                swap(my_array[j], my_array[j + 1]);
            }
        }
    }

    for (int i = 0; i < n - 1; i++)
    {
        for (int j = 0; j < n - i - 1; j++)
        {
            if (my_array[j].getY() < my_array[j + 1].getY() && my_array[j].getX() == my_array[j + 1].getX())
            {
                swap(my_array[j], my_array[j + 1]);
            }
            else
            {
                continue;
            }
        }
    }
    for (int i = 0; i < n; i++)
    {
        cout << my_array[i] << '\n';
    }

    return 0;
}