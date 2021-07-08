public class FactorCount {
    
    /** Creates a new instance of FactorCount */
    public FactorCount(int limit) {
        primes[1] = 2;  primes[2] = 3; nPrimes = 2;
        int cnt = 0;
        for (int i = 1; cnt <= limit; i++){
            if (i % 2 == 0) cnt = count(i / 2) * count (i+1);
            else cnt = count(i) * count((i+1)/2);
            if (cnt > 500) 
                answer = i;
        }
    }
    
    private int answer = 0;
    private int[] primes = new int[2000];
    private int nPrimes = 0;
    
    private int count(int n) {
        int[] prCnts = new int[2000];
        int high = 0;
        int i, j;
        for (i = 1; n > 1; i++) {
            if (i > nPrimes) {
                for (j = nPrimes + 1; j <= i; j++) {
                    primes[j] = getNextPrime(primes[j-1]);
                }
                nPrimes = i;
            }
            int p = primes[i];
            while (n % p == 0) {
                high = i;
                n /= p; prCnts[i]++;
            }
        }
        int result = 1;
        for (i = 1; i <= high; i++)
            if (prCnts[i] > 0)
                result *= (prCnts[i] + 1);
        return result;
    }
    
    private int getNextPrime(int n){
        int p = n+2;
        boolean hasDiv;
        int root, i;
        do {
            hasDiv = false;
            root = (int) Math.sqrt(p);
            for (i = 1; primes[i] <= root; i++){
                if (p % primes[i] ==0){
                    hasDiv = true; 
                    p += 2;
                    break;
                }
            }
        } while (hasDiv);
        return p;
    }
    
    int getAnswer(){return answer;}
    
    public static void main(String[] args){
        long start = System.currentTimeMillis();
        int n = new FactorCount(500).getAnswer();
        long stop = System.currentTimeMillis();
        System.out.println("" + n + "\t"+ n*(n+1)/2 + "\tTime: " + (stop-start) + "ms");
    }
    
}