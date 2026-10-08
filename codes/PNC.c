//Code by Arjun
//Date: 02-10-26
#include <stdio.h>
//main function begins
int main(void){

int p[] = {2, 3, 5, 7}; //all single digit primes
int count = 0;
int n=sizeof(p)/sizeof(p[0]); //Number of single digit primes

//main logic
for (int i = 0; i < n; i++){
for (int j = 0; j < n; j++){
for (int k = 0; k < n; k++){
if (i != j && j != k && i != k){
count++;}
}
}
}

	
//Output
printf("There are %d three digit numbers", count);

return 0;
}
