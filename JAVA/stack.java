
//similar to array
       /* arr.add(10),arr.remove(index:0),arr.get(0),arr.size()
          */
/*public class stack {
    public static void main(String[] args) {
        ArrayList<Integer> arr=new ArrayList<Integer>();
        arr.add(10);
        arr.add(20);
        arr.add(30);
        arr.add(40);
        arr.add(50);
        arr.remove(0);
        System.out.println(arr.get(0));
        System.out.println(arr.size());
        System.out.println(arr);
    }
} */
import java.util.ArrayList;
class Stac{
    ArrayList<Integer> stk=new ArrayList<Integer>();
    int size =5;
    public void push(int e){
        if(stk.size()==size){
            System.out.println("Overflow: stack is full");
        }
        else{
            stk.add(e);
        }
    }
    public void pop(){
        if(isEmpty()){
            System.out.println("Underflow: stack is empty");
        }
        else{
            stk.remove(stk.size()-1);
        }
    }
    //no peek for queue 
        public int peek(){
        if(!isEmpty()){
            return stk.get(stk.size()-1);
        }
        else {
            System.out.println("Stack is Empty");
            return -1;
        }
    }
    public boolean isEmpty(){
        if(stk.size()==0){
            return true;
        }
        return false;
    }
    public void printStack(){
        System.out.println(stk);
    }
    public void rev(){
        
    }
          }
        public class stack{
            public static void main(String[] args) {
                Stac ob=new Stac();
                ob.push(10);
                ob.push(20);
                ob.push(30);
                ob.printStack();
                ob.pop();
                ob.printStack();
                ob.push(0);
                System.out.println(ob.peek());
                ob.printStack(); 
            }
        }        