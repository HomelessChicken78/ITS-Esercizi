package java3.design_pattern.decorator;

public class EncryptionDecorator extends DataSourceDecorator {

	public EncryptionDecorator(DataSource source) {
		super(source);
	}

	@Override
	public void writeData(String data) {
		String res = "";
		for (int i = 0; i < data.length(); i++) {
			char questo = data.charAt(i);
			char prossimo = (questo >= 'a' && questo <= 'z') || (questo >= 'A' && questo <= 'Z') ? (char) (questo + 1) : questo;

			if (questo >= 'a' && questo <= 'z' && prossimo > 'z')
				prossimo = 'a';
			else if (questo >= 'A' && questo <= 'Z' && prossimo > 'Z')
				prossimo = 'A';

			res += prossimo;
		}

		// System.out.println("[Encrypt]: Sto per scrivere -> " + res);
		getSource().writeData(res);
	}

	@Override
	public String readData() {
		// System.out.println("[Encrypt]: Ho letto -> " + getSource().readData());
		String data = getSource().readData();
		String res = "";
		for (int i = 0; i < data.length(); i++) {
			char questo = data.charAt(i);
			char prossimo = (questo >= 'a' && questo <= 'z') || (questo >= 'A' && questo <= 'Z') ? (char) (questo - 1) : questo;

			if (questo >= 'a' && questo <= 'z' && prossimo < 'a')
				prossimo = 'z';
			else if (questo >= 'A' && questo <= 'Z' && prossimo < 'A')
				prossimo = 'Z';

			res += prossimo;
		}

		// System.out.println("[Encrypt]: (read) Sto per ritornare -> " + res + " - return cls: " + getSource().getClass().getSimpleName());
		return res;
	}
}
