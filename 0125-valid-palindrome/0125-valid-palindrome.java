class Solution {
    public boolean isPalindrome(String s) {
        String lower = s.toLowerCase();

        String clean = lower.replaceAll("[^a-zA-Z0-9]", "");

        char[] charArray = clean.toCharArray();
        int start = 0;
        int end = charArray.length - 1;
        while(start<end){
            char temp = charArray[start];
            charArray[start] = charArray[end];
            charArray[end] = temp;
            start++;
            end--;
        }
        String reversed = new String(charArray);
        if(clean.equals(reversed)){
            return true;   
        }
        else{
            return false;  
        }

    }
}