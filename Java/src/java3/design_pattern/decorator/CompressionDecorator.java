package java3.design_pattern.decorator;

public class CompressionDecorator extends DataSourceDecorator {
	public CompressionDecorator(DataSource source) {
		super(source);
	}

	@Override
	public void writeData(String data) {
		String res = "";

		for (int i = 0; i < data.length(); i++) {
			String ch = String.valueOf(data.charAt(i));

			if (!ch.equals(" "))
				res += ch;
		}

		// System.out.println("[Compression]: Sto per scrivere -> " + res.toLowerCase());
		getSource().writeData(res.toLowerCase());
	}

	@Override
	public String readData() {
		// System.out.println("[Compression]: Ho letto e ritorno -> " + getSource().readData() + " - return cls: " + getSource().getClass().getSimpleName());
		return getSource().readData();
	}

}
