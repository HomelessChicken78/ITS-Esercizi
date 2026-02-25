package java3.design_pattern.factory;

import java.io.*;
import java.util.List;

public class CsvExporter implements DataExport {

	@Override
	public void export(List<String> data, String fileName) {
		String risultato = data.stream().reduce("\n", (a, b) -> a + ", " + b) + "\n";

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
		return "text/csv";
	}

}
