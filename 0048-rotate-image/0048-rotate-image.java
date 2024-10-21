class Solution {
    public void rotate(int[][] matrix) {
        int n = matrix.length;
        //we will first find the transpose
        for(int i=0; i<n; i++){
            for(int j=0; j<i; j++){
                int temp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = temp;
            }
        }

        for(int i=0; i<n; i++){
            int p=0, q=n-1;
            while(p<q){
                int temp = matrix[i][p];
                matrix[i][p] = matrix[i][q];
                matrix[i][q] = temp;
                p++;
                q--;
            }
        }
    }
}