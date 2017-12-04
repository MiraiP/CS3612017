/**
 * @author Christelle
 * 
 */
public class ScannerDemo {

	private static String file1 = "C:\\Users\\Brandon\\workspace\\ParserScannerTests\\SCANNER\\prog1.jay";
	private static int i = 1;

	public static void main(String args[]) {

		TokenStream ts = new TokenStream(file1);
		Token t;
		

		//System.out.println(file1);

		while (!ts.isEndofFile()) {
			t = ts.nextToken();

			System.out.println("Token " + i + " - " + "Type: " + t.getType() + " - " + "Value: " + t.getValue());
			
		//	if (t == null) {
		//		System.out.println("Token is null");
		//	} else{
		//		System.out.println("Token is not null");
		//	}
			
			i = i + 1;
			
		}
	}
}

//Token i - Type: thetype - Value: thecontent