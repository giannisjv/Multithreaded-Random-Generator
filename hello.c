#include <stdio.h>
#include <omp.h>

int main(int argc, char const *argv[])
{
    int cores = omp_get_max_threads();
    printf("\n%d\n", cores);

    #pragma omp parallel for schedule(guided, 1) num_threads(4)
        for (int i = 0; i < 20; i++)
        {
            printf("core %d\n", omp_get_thread_num());
        }

    return 0;
}
