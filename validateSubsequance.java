public class validateSubsequance {
    public static boolean validateSubseqence(int[] array, int[] subsequence){
        int arrIdx = 0;
        int seqIdx = 0;

        while(arrIdx < array.length && seqIdx < subsequence.length){
            if(array[arrIdx] == subsequence[seqIdx]){
                seqIdx++;
            }
            arrIdx++;
        }

        return seqIdx == subsequence.length;
    }
    public static void main(String[] args){
        System.out.println(validateSubseqence(new int[] {5,1,22,25,6,-1,8,10}, new int[] {1,6,-1,10}));
    }
}
