import java.util.Arrays;

public class arrayOfProducts {
    public static int[] arrayOfProducts(int[] array){
        int[] products = new int[array.length];
        int[] lftProducts = new int[array.length];
        int[] rgtProducts = new int[array.length];

        int lftRunningProduct = 1;
        for(int i=0; i < array.length; i++){
            lftProducts[i] = lftRunningProduct;
            lftRunningProduct *= array[i];
        }

        int rgtRunningProduct = 1;
        for(int i=array.length-1; i >= 0; i--){
            rgtProducts[i]  = rgtRunningProduct;
            rgtRunningProduct *= array[i];
        }

        for(int i=0; i<array.length; i++){
            products[i] = lftProducts[i] * rgtProducts[i];
        }
        return products;
    }
    public static void main(String[] args){
        System.out.println(Arrays.toString(arrayOfProducts(new int[] {5,1,4,2})));
    }
}
