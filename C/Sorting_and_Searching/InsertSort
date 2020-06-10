#include<stdio.h>

void InsertSort(int a[], int alength){
    /**
     * @param a: 待排序数组
     * @param alength: 数组的长度
     */
    int j = 0;
    for (int i = 1; i < alength;i++){
        int cur = a[i]; // 存储待插入值
        for (j = i - 1; j >= 0 && a[j]>cur;j--){
            a[j + 1] = a[j]; // 后移一位
        }
        a[j + 1] = cur;
    }
}

int main(){
    int a[6] = {2,5,4,7,8,6};
    int n = sizeof(a) / sizeof(a[0]);
    InsertSort(a, n);
    for (int i = 0; i < n;i++){
        printf("%d,", a[i]);
    }
}
