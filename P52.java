import java.util.Vector;

public class P52{

    public boolean isSubset(int x[], int y[]) {
        boolean isSub = false;
        int same=0;
        for (int i=0;i<x.length;i++) {
            for (int j=0;j<y.length;j++) {
                if (x[i] == y[j]) {same++;}
            }
        }
        if (same >= x.length) {isSub=true;}
        return isSub;
    }

    public Vector<Integer> getNums(int n) {
        //int nums[] = new int[1];
        Vector<Integer> v = new Vector();
        while (n!=0) {
            v.add(n%10);
            n/=10;
        }
        return v;
    }

    public void get() {
        int i=1, j=1, matches, t[][];
        boolean notGet = true;
        while (notGet && i<10000) {
            matches=0;
            Vector<Integer> temp = new Vector<Integer>();
            while (j<=6) {
                temp = getNums(i*j);
                t[i-1] = new int[temp.length];
                for (int q=0;q<temp.length;q++) {
                    t[i-1][q] = temp.get(q);
                }
                j++;
            }
            j=1;
            while (j<=6) {
                if (isSubset(x, y))
            }
        }
    }

    public static void main(String args[]) {
        P49 p = new P49();
        p.get();
        //p.Print();
        //System.out.println(p.digitsCompare(1234,4321,2341));
        //System.out.println(p.digitsCompare(1234,1234,1234));
    }
}