#include<stdio.h>
#include<conio.h>
#include<iostream>
using namespace std;

int findSum() {
    int sum = 0;
    cout<<"summing up";
    for (int v = 1; v <= 900000000; v++) {
        sum += v;
    }
    printf("sum: %d", sum);
    return sum;
}
int sum() {
    int N = 900000000; //900 Million
    return N * (N + 1) / 2;
}
int main(){
	int x = findSum();
//	int y = sum(900000000);
//	cout<<y;
//	900Millions
}
