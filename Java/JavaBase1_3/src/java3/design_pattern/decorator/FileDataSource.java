package java3.design_pattern.decorator;

public class FileDataSource implements DataSource {
	private String content = "";
	public FileDataSource() {
	}

	@Override
	public void writeData(String data) {
		content = data;
	}

	@Override
	public String readData() {
		return content;
	}
}
