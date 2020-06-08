package pres.eao.algorithm.sorting.searching;

public class InsertionSort {
	public static void main(String[] args) {
		int[] a = { 2, 6, 1, 4, 5, 3, 2 };

		int i = 0, j = 0;
		for (i = 1; i < a.length; i++) {
			int cur = a[i];
			for (j = i - 1; j >= 0 && a[j] >= cur; j--) { // 和已排序的对比
				a[j + 1] = a[j];  // 后移一位
			}
			a[j + 1] = cur;
		}
		
		for (int k : a) {
			System.out.print(k + " ");
		}
	}
}