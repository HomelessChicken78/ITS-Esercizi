package java3.design_pattern.decorator;

public interface DataSource {
	void writeData(String data);
	String readData();
}
