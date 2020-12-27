import java.util.Arrays;

public class smallestDifference {
    public static int[] smallestDifference(int[] arrayOne, int[] arrayTwo){
        Arrays.sort(arrayOne);
        Arrays.sort(arrayTwo);
        int idxOne = 0;
        int idxTwo = 0;
        int current = Integer.MAX_VALUE;
        int smallest = Integer.MAX_VALUE;
        int[] smallestPair = new int[2];
        while (idxOne < arrayOne.length && idxTwo < arrayTwo.length){
            int firstNum = arrayOne[idxOne];
            int secondNum = arrayTwo[idxTwo];

            if (firstNum < secondNum){
                current = secondNum - firstNum;
                idxOne++;
            }
            else if (secondNum < firstNum){
                current  = firstNum - secondNum;
                idxTwo++;
            }
            else {
                return new int[] {firstNum, secondNum};
            }
            if (current < smallest){
                smallest = current;
                smallestPair = new int[] {firstNum, secondNum};
            }
        }
        return smallestPair;
    }
    public static void main (String[] args){
        System.out.println(Arrays.toString(smallestDifference(new int[]{-1,3,5,10,20,28},new int[]{15,17,26,134,135})));
    }
}
