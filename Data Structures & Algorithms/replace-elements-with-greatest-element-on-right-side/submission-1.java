class Solution {
    public int[] replaceElements(int[] arr) {
        
        int[] res = new int[arr.length];

        

        for(int i = 0; i < arr.length; i++){

            int maxR = 0;    
            

            for(int j = i + 1; j< arr.length; j++){

                if(arr[j] > maxR){
                    maxR = arr[j];
                }
            }

            res[i] = maxR; 
            
        }

        res[res.length -1] = -1;

        return res;

    }
}