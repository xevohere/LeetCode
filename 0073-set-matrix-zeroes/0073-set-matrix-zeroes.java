class Solution {
    public void setZeroes(int[][] matrix) {
        
        //int[][] arr = matrix.clone();
        int[][] arr = new int[matrix.length][matrix[0].length];
        
        for(int i=0; i<matrix.length; i++){
            for(int j=0; j<matrix[0].length; j++){
                arr[i][j]=matrix[i][j];
            }
        }
            
        for(int i=0; i<matrix.length; i++){
            for(int j=0; j<matrix[0].length; j++){
                if(arr[i][j]==0){
                    for(int p=0; p<matrix.length; p++){
                        matrix[p][j]=0;
                    }
                    for(int q=0; q<matrix[0].length; q++){
                        matrix[i][q]=0;
                    }
                }
            }
        }
    }
}