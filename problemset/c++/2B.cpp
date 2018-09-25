#include <cstdio>
#include <string>

const int N = 1002;
int n;
int counts[N][N][2] = {0};
char path[2*(N-1)];
int zx = -1;
int zy = -1;

// note that the only way to get a zero is if we multiply by a number
// that has at least one factor of 2 and 5, so we will want to count
// these with count_facs on each element of A
void count_facs(int x, int f, int i, int j, int p) {
    while (x > 0 && x % f == 0) {
        x /= f;
        counts[i][j][p]++;
    }
}

// we must account for the case that a zero shows up, if so we
// automatically know we can get a solution with just 1 zero since
// 0*(any number) = 0, so we just take the path going through it
// the only way to beat this is if we have a path with no trailing
// zeros
void print_results(int p)
{
    if (zx > 0 && counts[n-1][n-1][p] > 0){
        printf("%d\n", 1);
        for (int i = 0; i < zy; i++) { printf("%s", "D"); }
        for (int j = 0; j < zx; j++) { printf("%s", "R"); }
        for (int i = zy + 1; i < n; i++) { printf("%s", "D"); }
        for (int j = zx + 1; j < n; j++) { printf("%s", "R"); }
    } else {
        printf("%d\n", counts[n-1][n-1][p]);
        int pos = 2*(n-1) - 1;
        int i = n - 1;
        int j = n - 1;
        while (i + j > 0) {
            if (i > 0 && j > 0) {
                if (counts[i][j-1][p] < counts[i-1][j][p]) {
                    path[pos] = 'R';
                    j -= 1;
                } else {
                    path[pos] = 'D';
                    i -= 1;
                }
            } else if (i == 0) {
                path[pos] = 'R';
                j -= 1;
            } else {
                path[pos] = 'D';
                i -= 1;
            }
            pos -= 1;
        }

        for (int i = 0; i < 2*(n-1); i++) {
            printf("%c", path[i]);
        }
    }
}

// the following function will find for each i and j the path
// in which the numbers 2 & 5 (separately) show up in the product
// the least amount of times
void dp() {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            int Aij = 0;
            scanf("%d", &Aij);
            if (!Aij) {
                zx = j;
                zy = i;
            }
            count_facs(Aij, 2, i, j, 0);
            count_facs(Aij, 5, i, j, 1);
            if (i > 0 && j > 0) {
                counts[i][j][0] += std::min(counts[i][j-1][0], counts[i-1][j][0]);
                counts[i][j][1] += std::min(counts[i][j-1][1], counts[i-1][j][1]);
            } else if (i > 0 && j == 0) {
                counts[i][j][0] += counts[i-1][0][0];
                counts[i][j][1] += counts[i-1][0][1];
            } else if (i == 0 && j > 0) {
                counts[i][j][0] += counts[0][j-1][0];
                counts[i][j][1] += counts[0][j-1][1];
            }
        }
    }
}

int main()
{
    scanf("%d", &n);
    dp();
    print_results(counts[n-1][n-1][0] > counts[n-1][n-1][1]);
    return 0;
}
