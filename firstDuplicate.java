public class firstDuplicate {
    public static int firstDuplicate(int[] array){
        for(int i=0; i<array.length; i++){
            if(array[Math.abs(array[i]) - 1] < 0){
                return Math.abs(array[i]);
            }
            array[Math.abs(array[i])-1] *= -1;
        }
        return -1;
    }
    public static void main(String args[]){
        System.out.println(firstDuplicate(new int[] {2,1,5,3,3,2,4}));
    }
}
