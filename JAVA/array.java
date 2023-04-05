import java.util.*;
public class array {
    public static void main(String[] args) {
        System.out.println("enter n");
        Scanner Sc=new Scanner(System.in);
        int n=Sc.nextInt();
        int arr[]=new int[n];
        System.out.println("enter array elements");

        int i;
        for(i=0;i<n;i++){
            arr[i]=Sc.nextInt();
        }

       
        for(int num:arr){
            System.out.print(num+" ");

        }
        Sc.close();
    }
}
