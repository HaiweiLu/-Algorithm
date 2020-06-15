#include<stdio.h>

void sort(int s[], int f[], int n){
    /*
     * 按活动结束时间从早到迟排序——插入排序
     */
    int j = 0;
    for (int i = 1; i < n;i++){
        int fcur = f[i];
        int scur = s[i];
        for (j = i - 1; j >= 0 && fcur < f[j] ;j--){
            f[j+1] = f[j];
            s[j + 1] = s[j];
        }
        f[j+1] = fcur;
        s[j + 1] = scur;
    }
    printf("活动按结束时间排序后如下：\n");
    for (int i = 0; i < n;i++){
        printf("第[%d]个活动(开始,结束)时间: %d, %d \n", i+1, s[i], f[i]);
    }
}

int greedy(int s[], int f[], bool a[], int n){
    /**
     * param s : 活动起始时间
     * param f : 活动结束时间
     * param a : 安排活动
     * param n : 总活动数量
     */
    sort(s, f, n);
    a[0] = true; // 默认第一个活动被安排
    int count = 1; // count 记录选择的活动数量
    for (int i = 1, j = 0; i < n;i++){
        /**
         * 贪心策略：取当前活动集合中结束时间最早的相容活动，这样可以为未安排的活动留下心网能多的时间，
		 * 也就是说，这种贪心选择的目的是使剩余时间段极大化，以便安排尽可能多的相容活动。
         */

        if(s[i]>f[j]){ // 选择函数——后一个活动的开始时间 晚于 前一个活动的结束时间
            a[i] = true;
            j = i;
            count++;
        }
        else{
            a[i] = false;
        }
    }
    return count;
}


int main(){
    int n = 11;
    int start[n] = {1,3,0,5,3,6,8,8,2,12};
    int end[n] = {4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14};
    
    bool a [n] = {};
    int num = greedy(start, end, a, n);
    printf("活动总数 = %d\n选择活动：", num);
    for (int i = 0; i < n;i++){
        if(a[i] == true){
            printf("%d\t", i+1);
        }
    }
}

//输出如下：
活动按结束时间排序后如下：
第[1]个活动(开始,结束)时间: 1, 4
第[2]个活动(开始,结束)时间: 3, 5
第[3]个活动(开始,结束)时间: 0, 6
第[4]个活动(开始,结束)时间: 5, 7
第[5]个活动(开始,结束)时间: 3, 8
第[6]个活动(开始,结束)时间: 6, 9
第[7]个活动(开始,结束)时间: 8, 10
第[8]个活动(开始,结束)时间: 8, 11
第[9]个活动(开始,结束)时间: 2, 12
第[10]个活动(开始,结束)时间: 12, 13
第[11]个活动(开始,结束)时间: 0, 14
活动总数 = 4
选择活动：1     4       7       10
//
