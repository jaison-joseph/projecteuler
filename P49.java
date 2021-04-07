
public class P49 {
    int primes[], len, num_len, num, longest_num_len, i, j, k;

    public P49() {
        longest_num_len=0;
        primes = new int[2000];
        len=2;
        primes[0]=2;
        primes[1]=3;
        for (i=5;i<10000;i+=2) {
            int prime=1;
            j = 3;
            while (prime == 1 && j<=Math.sqrt(i)) {
                if (i%j == 0) {prime=0;}
                j += 2;
            }
            if (prime == 1) {primes[len]=i; len++;}
        }
        System.out.println("Length: "+ len);
    }

    public Boolean isPrime (int no) {
        Boolean p = true;
        int z=0;
        while (p && primes[z]<=Math.sqrt(no)) {
            if (no%primes[z]==0) {
                //System.out.println("Divisor: "+ primes[z]);
                p=false;
            }
            z++;
        }
        return p;
    }

    public void Print() {
        for (i=0;primes[i]<100;i++) {
            System.out.println(primes[i]);
        }
    }

    public void get() {
        int ii=0;
        while (primes[ii]<=1000) {ii++;}
        //System.out.println(primes[i]);
        
        while (primes[ii]<=3339 && ii<len) {
            //System.out.println(primes[i]);
            
            if (isPrime(primes[ii]+3330) && isPrime(primes[ii]+6660) && primes[ii]>1000) {
                //System.out.println(ii);
                //System.out.println(primes[ii] + ", "+ (primes[ii]+3330) + ", " + (primes[ii]+6660));
                if (  digitsCompare( primes[ii],(primes[ii]+3330),(primes[ii]+6660) )  ) {
                    System.out.println(primes[ii] + ", "+ (primes[ii]+3330) + ", " + (primes[ii]+6660));
                }   
            }
            ii++; 
        }
        
    }

    public Boolean digitsCompare(int x1, int x2, int x3) {
        //int n1[], n2[], n3[];

        //System.out.println(x1 + ", "+ x2 + ", " + x3);

        Boolean isPermu=false;
        int n[] = new int[12];
        int nos[] = {x1,x2,x3};
        for (i=0;i<3;i++) {
            for (j=0;j<4;j++) {
                n[j+4*i]=nos[i]%10;
                //System.out.println(n[j+i]);
                nos[i]/=10;
            }
        }
        

        int matches=0;
        for (i=0;i<4;i++) {
            for (j=4;j<8;j++) {
                if (n[i] == n[j+4]) {
                    //System.out.println("x");
                    for (k=8;k<12;k++) {
                        //System.out.println(i + '.' + j + '.' + k + " :: "+ n[i] + ", " + n[j]+ ", " + n[k]);
                        if(n[k]==n[i]) {
                            matches++;
                        } 
                    }
                }
            }
        }
        //System.out.println("Matches: " + matches);
        if (matches >=3) {isPermu = true;}

        return isPermu;
    }

    public static void main(String args[]) {
        P49 p = new P49();
        p.get();
        //p.Print();
        //System.out.println(p.digitsCompare(1234,4321,2341));
        //System.out.println(p.digitsCompare(1234,1234,1234));
    }
}