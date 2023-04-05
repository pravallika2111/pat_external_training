
public class palindrom {
    public static void main(String[] args) {
        System.out.print("enter n");
        int arr[]=new int[3];
        arr[0]=100;
        arr[1]=101;
        arr[2]=121;
        for(int n:arr){  
            int d,s1=0,c=n;
            while(n>0){
                d=n%10;
                s1=s1*10+d;
                n=n/10;
            }
            System.out.println(s1);
            if(s1==c){
                System.out.println("Palindrom");
            }
            else{
                System.out.println("not Palindrom");
            }
        }
    }
    
}
