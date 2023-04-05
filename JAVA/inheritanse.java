class Library{
   /*  String name1="i am A";
    public  void welcome(){
        System.out.println("welcome A");
        
    }*/
    int id=45;
    String name="sai";
}
//single level
class Student1 extends Library{
   /*  String name2="i am B";
    public  void Home(){
        System.out.println("welcome B");
        
    }*/
    public void Student(){
        System.out.println("Student");
    }

}
//multilevel A-->B B-->C
class C extends Student1{

}
//hirechical A-->B A-->D
class Faculty1 extends Library{

    public void Faculty(){
        System.out.println("Faculty");
    }
}
public class inheritanse {
    public static void main(String[] args) {
        Student1 b=new Student1();
        System.out.println(b.id);
        b.Student();
       
    }
    
}
