package java3.design_pattern.factory;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.List;

public class JsonExporter implements DataExport {
	@Override
	public void export(List<String> data, String fileName) {
		String risultato = "\n{\n\t" + data.stream().reduce((a, b) -> a + "\n\t" + b) + "\n}";

		try {
			BufferedWriter bf = new BufferedWriter(new FileWriter(fileName, true));
			bf.write(risultato);
			bf.close();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}

	@Override
	public String getMime() {
		return "application/json";
	}
}
