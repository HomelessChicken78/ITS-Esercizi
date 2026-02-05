package java3.stream.esercizi.another;

import java.util.List;
import java.util.stream.Collectors;

public class Short {
	public static void main(String[] args) {
		List<Integer> numeri = List.of(3, 10, 7, 2, 8, 15, 4);
		List<Integer> res = numeri.stream().filter(n -> n % 2 == 0)
		.collect(Collectors.toList());

		System.out.println(res);

		List<String> nomi = List.of("luca", "maria", "anna", "giovanni");
		List<String> res2 = nomi.stream()
				.map(p -> p.toUpperCase())
				.collect(Collectors.toList());

		System.out.println(res2);

		List<String> parole = List.of("java", "stream", "lambda", "java", "stream");
		long res3 = parole.stream()
				.filter(p -> p.length() > 4)
				.count();
		System.out.println(res3);

		List<Integer> altriNumeri = List.of(1, 2, 3, 4, 5);
		int res4 = altriNumeri.stream()
				.reduce(0, (acc, n2) -> acc + n2);
		System.out.println(res4);

		List<String> città = List.of("Roma", "Milano", "Roma", "Torino", "Milano");
		List<String> res5 = città.stream()
				.distinct()
				.sorted()
				.collect(Collectors.toList());
		System.out.println(res5);
	}
}
