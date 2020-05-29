import java.util.*;
import java.lang.*;
import java.io.*;
class trie
{
  HashMap<Character,trie> child;;
  boolean isEnd;
  trie()
  {
    isEnd=false;
    child=new HashMap<>();
  }
  void add(String a,trie root)
  {
  trie cur=root;
  for (int i=0;i<a.length() ;++i ) {
    if(cur.child.containsKey(a.charAt(i)))
    cur=cur.child.get(a.charAt(i));
    else
    {cur.child.put(a.charAt(i),new trie());
      cur=cur.child.get(a.charAt(i));
    }
  }
  cur.isEnd=true;
  }
   void search(String a,trie root)
   {
     trie cur=root;
     for (int i=0; i<a.length();++i ) {
       char t=a.charAt(i);
       trie node=cur.child.get(t);
       if(node==null)
       {System.out.print("0");
     return;}

     cur=node;
     }
     print(cur,a);
   }
   void print(trie root,String prefix)
   {
       if(root.isEnd)
       {System.out.print(prefix+" ");
       }
     for(char i='a';i<='z';++i)
     {
       trie node=root.child.get(i);
       
       if(node!=null)
       print(node,prefix+i);
     }
   }
}
class phoneDict
 {
  static trie root;
  public static void fn(String a[],int n,String q)
  {
    for (String t :a ) {
      root.add(t,root);
    }
    for(int i=1;i<=q.length();++i)
    {root.search(q.substring(0,i),root);
      System.out.println();
    }
  }
 public static void main (String[] args)
  {
 Scanner ab=new Scanner(System.in);
 int t=ab.nextInt();
 while(t-->0)
 {
     root=new trie();
     int n=ab.nextInt();
     String arr[]=new String[n];
     for(int i=0;i<n;++i)
     arr[i]=ab.next();
      fn(arr,n,ab.next());
     //System.out.println();
 }
  }
}
