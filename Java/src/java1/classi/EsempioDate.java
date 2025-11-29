package java1.classi;

import java.util.Date;

public class EsempioDate {
	@SuppressWarnings("deprecation")
	public static void main(String[] args) {
		Date d = new Date();
		
		System.out.println(d.toString());
		System.out.println(d);
		
		System.out.println(d.getYear()); // deprecated
		System.out.println(d.getMonth()); // deprecated
		
		d.setMonth(12); // -> Month 0 (Jan) of the next year
		System.out.println(d);
		
		Date christmas = new Date(125, 11, 25); // Set to default the missing attributes
		
		System.out.println(christmas);
	}
}
