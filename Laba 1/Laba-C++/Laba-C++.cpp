#include "Func.h"

int main()
{
    int t1 = time(NULL);
    //createfile();
    start();
    int t2 = time(NULL);
    cout << "\nThe time of the program's work: " << t2 - t1 << "s" << endl;
}