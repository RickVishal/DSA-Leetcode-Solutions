class Solution:
    def rotate(self, arr: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        col_len=len(arr[0])
        row_len=len(arr)
        for i in range(row_len):
            for j in range(col_len):
                if j<i:
                    arr[i][j],arr[j][i]=arr[j][i],arr[i][j]
        for i in range(row_len):
            arr[i].reverse()