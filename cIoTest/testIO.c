#include <stdio.h>
#include <stdlib.h>

int main(void) {
    FILE* ofp = fopen("test.txt", "w+");
    if (ofp == NULL) {
        fprintf(stderr, "Can't open output file %s!\n",
          "test.txt");
        exit(1);
    }

    double arr[5] = {1e2, 1e3, 2.21e4, 1e5, 1e6};
    //fwrite(arr, 17, sizeof(arr), ofp);
    for (int i=0; i<5; i++) {
        fprintf(ofp,"%f\n", arr[i]);
    }

    fclose(ofp);

   FILE* ifp = fopen("test.txt", "r");
   double newarr[5];

   for (int i = 0; i < 5; i++) {
    fscanf(ifp, "%lf", &arr[i]);
   }
   fclose(ifp);

   printf("%f\n", arr[4]);


}