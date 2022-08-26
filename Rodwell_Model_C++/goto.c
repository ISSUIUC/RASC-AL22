#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <unistd.h>

int main(void) {
    int i;
    for(i = 1; i < 10; i++) {
        printf("inside i = %d\n", i);
        goto out;
inend: //when it jumps here it ignores the for loop, all for loop data is lost
        printf("back into\n");
        //continue;
    }
out:
        printf("outside i = %d\n", i);
        goto inend;
    
    
    return 0;
}
