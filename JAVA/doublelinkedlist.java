class Node{
    int data;
    Node next;
    Node prev;

    public Node(int value){
        this.data=value;
        next=null;
        prev=null;
    }

}
class LL{
 
public void addElement(Node head,int data){
    Node new_node=new Node(data);
    Node cur=head;
    while(cur.next!=null){
        cur=cur.next;
    }
    cur.next=new_node;
    new_node.prev=cur;
}
public void deleteElement(){
    
}
public void print(Node head){

    Node cur=head;
    while(cur!=null){
        System.out.println(cur.data);
        cur=cur.next;
    }
}}
public class doublelinkedlist {
    public static void main(String[] args) {
        LL h=new LL();
    Node head=new Node(20);
    h.addElement(head,20);
    h.addElement(head,40);
    h.addElement(head,50);
    h.print(head);
    

    }
}
