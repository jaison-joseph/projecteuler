public class P50 {
    int primes[], len, num_len, num, longest_num_len, i, j, k;

    public P50() {
        longest_num_len=0;
        primes = new int[80000];
        len=2;
        primes[0]=2;
        primes[1]=3;
        for (i=5;i<1000000;i+=2) {
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

    public void get() {
        int sum;
        for (i=0;i<len-1;i++) {
            sum = primes[i];
            num_len=1;
            j=i+1;
            while (j<len & (sum+primes[j]) < 1000000) {
                sum += primes[j];
                //System.out.println("i: " + i + ":: j: " +j + ":: sum: " +sum);
                num_len ++;
                k=0;
                int prime = 1;
                while (prime == 1 && primes[k]<=Math.sqrt(sum)) {
                    if (sum%primes[k]==0) {prime=0;}
                    k++;
                }
                if (prime == 1 && num_len>longest_num_len) {
                    longest_num_len = num_len;
                    num = sum;
                }
                j++;
            }
        }
        System.out.println(longest_num_len + ": "+ num);
    }
    public static void main(String args[]) {
        P50 p = new P50();
        p.get();
    }
}