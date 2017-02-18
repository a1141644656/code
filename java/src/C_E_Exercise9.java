// by C.W.B
// Fibonacci sequence

public class C_E_Exercise9 {
	public static void main(String[] args) {
		Fibonacci_sequence(20);
		System.out.println();
		
		fib_recursion(20);
		System.out.println();
		
		Binet_formula(20);
		System.out.println();
	}
	
	static void Fibonacci_sequence(int num) {
		if(num < 1) {
			System.out.println("None");
			return;
		}
		else
			System.out.print(1 + " ");
		
		int temp1 = 0;
		int temp2 = 1;
		int temp;
		for(int i = 1; i < num; i++) {
			temp = temp1 + temp2;
			System.out.print(temp + " ");
			temp1 = temp2;
			temp2 = temp;
		}
	}
	
	static int fib(int n) { 
		if(n <= 2)
			return 1; 
		return fib(n-1) + fib(n-2); 
	}
	static void fib_recursion(int n) {
		for(int i = 1; i <= n; i++)
			System.out.print(fib(i) + " ");
	}
	
	static void Binet_formula(int n) {
		for(int i = 1; i <= n; i++) {
			int fib = (int)Math.round(1 / Math.sqrt(5) * (Math.pow((1 + Math.sqrt(5)) / 2, i) - Math.pow((1 - Math.sqrt(5)) / 2, i)));
			System.out.print(fib + " ");
		}
	}
}
