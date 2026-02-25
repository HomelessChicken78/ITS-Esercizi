package java3.design_pattern.factory;

public class FactoryDataExport {
	@SuppressWarnings("deprecation")
	public static DataExport getExport(String dataExportType) throws ClassNotFoundException {
		Class<?> createdExporter = null;
		createdExporter = Class.forName(dataExportType);

		try {
			return (DataExport) createdExporter.newInstance();
		} catch (InstantiationException | IllegalAccessException e) {
			e.printStackTrace();
		}
		return null;
	}
}
