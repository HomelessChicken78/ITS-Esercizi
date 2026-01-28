package java3.design_pattern.decorator;

public class Test_Decorator {
	public static void main(String[] args) {
		FileDataSource f = new FileDataSource();
		EncryptionDecorator encr = new EncryptionDecorator(f);

		encr.writeData("[ZCiao] dice \"bella\"");
		System.out.println(encr.readData());



		FileDataSource f2 = new FileDataSource();
		CompressionDecorator compr = new CompressionDecorator(f2);

		compr.writeData("Ciao a TUTTI ragazzi");
		System.out.println(compr.readData());



		FileDataSource f3 = new FileDataSource();
		Base64Decorator b64 = new Base64Decorator(f3);

		b64.writeData("Giacomo e me");
		System.out.println(b64.readData());



		System.out.println();
		EncryptionDecorator allDecorators = new EncryptionDecorator(new CompressionDecorator(new Base64Decorator(new FileDataSource())));
		allDecorators.writeData("Hi How ARE You!");
		System.out.println("" + allDecorators.readData());
	}
}
