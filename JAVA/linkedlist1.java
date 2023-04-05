class Node{
    int data;
    Node next;
    public Node(int value){
        this.data=value;
        next=null;

    }
}
class LL{
    public Node addElement(Node head,int data){
        Node new_node=new Node(data);
        //insert at begining
        Node temp=head;
        head=new_node;
        head.next=temp;
        return head;
    }


    public void deleteElement(Node head){
        Node cur=head;
        while(cur.next.next!=null){
            
            cur=cur.next;
        }
        cur.next=null;


    }
    public void printList(Node head){
        Node cur=head;
        while(cur!=null){
            System.out.println(cur.data);
            cur=cur.next;
        }

    }
}
public class linkedlist1{
    public static void main(String[] args) {
        LL h=new LL();
    Node head=new Node(10);
    h.addElement(head,20);
    h.addElement(head,30);
    h.addElement(head,40);
    h.printList(head);

    }



    
}


