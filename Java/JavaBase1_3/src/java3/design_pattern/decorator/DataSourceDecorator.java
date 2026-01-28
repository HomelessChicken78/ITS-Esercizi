package java3.design_pattern.decorator;

public abstract class DataSourceDecorator implements DataSource {
	private DataSource source;

	public DataSourceDecorator(DataSource source) {
		this.source = source;
	}

	@Override
	public abstract void writeData(String data);

	@Override
	public abstract String readData();

	public DataSource getSource() {
		return source;
	}
}
