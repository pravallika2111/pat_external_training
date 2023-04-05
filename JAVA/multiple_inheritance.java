//interface will not have body for methods,even if dont use method that is present in interface it should be written in class
// in interface variables,method are always public,static,
//because of dimond problem we can't use multiple inheritance directly so we use interface
interface A{
    public void Welcome();
    public void Something();
}
interface B{
    public void Welcome1();

}
class C implements A,B{
    public void Welcome(){
        System.out.println("welcome c");
    }
    public void Something(){

    }
    public void Welcome1(){

    }
    
}
public class multiple_inheritance {
    public static void main(String[] args) {
        C c=new C();
        c.Welcome();
        
    }
    
}
