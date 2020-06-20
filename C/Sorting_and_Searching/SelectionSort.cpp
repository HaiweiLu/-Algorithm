#include<stdio.h>

void SelectionSort(int a[], int n){
    /**
     * 选择排序
     * param a : 待排序数组
     */
    for (int i = 0; i < n;i++){
        int min = i; // 记录最小位置
        for (int j = i+1; j < n;j++)
            if(a[j]<a[min]){
                min = j; // 找到未排序数组中最小的那个数
            }
        int temp = a[i]; // 最小的数与其当前占据其位置的数交换
        a[i] = a[min];
        a[min] = temp;
    }
}

int main(){
    int a[6] = {2,5,4,7,8,6};
    int n = sizeof(a) / sizeof(a[0]);
    SelectionSort(a, n);
    printf("选择排序后：");
    for (int i = 0; i < 6 ;i++){
        printf("%d\t", a[i]);
    }
        return 0;
}
