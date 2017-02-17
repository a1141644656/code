// by C.W.B
// Fibonacci sequence

public class C_E_Exercise9 {
	public static void main(String[] args) {
		Fibonacci_sequence(10);
	}
	
	static void Fibonacci_sequence(int num) {
		if (num < 1) {
			System.out.println("None");
			return;
		}
		else
			System.out.print(1 + " ");
		
		int temp1 = 0;
		int temp2 = 1;
		int temp;
		for (int i = 1; i < num; i++) {
			temp = temp1 + temp2;
			System.out.print(temp + " ");
			temp1 = temp2;
			temp2 = temp;
		}
	}
}
