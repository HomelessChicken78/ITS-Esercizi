package com.spring.java.esercizi;

import java.time.LocalDate;
import java.time.Month;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping(path = "/stringhe")
public class Stringhe {
	Stringhe() {
	}

	@GetMapping(path = "/isNumeric")
	public String isNumeric(String str) {
		boolean all_numbers = true;
		for (int i = 0; i < str.length(); i++) {
			if (str.charAt(i) < '0' || str.charAt(i) > '9') {
				all_numbers = false;
				break;
			}
		}

		return all_numbers ? "testo numerico" : "testo NON numerico";
	}

	@GetMapping(path = "/convertiData")
	public String convertToDate(String str) {
		int day = Integer.parseInt(str.substring(0, 2));
		String month = Month.of(Integer.parseInt(str.substring(3, 5))).toString().toLowerCase();
		int year = Integer.parseInt(str.substring(6));

		// Crea localdate così che esegua i controlli autonomamente
		LocalDate date = LocalDate.of(year, Integer.parseInt(str.substring(3, 5)), day);

		return day + " " + month + " " + year;
	}

	@GetMapping(path = "/isPalindroma")
	public boolean isPalindroma(String str) {
		String reversedString = "";

		for (int i = str.length() - 1; i >= 0; i--) {
			reversedString += str.charAt(i);
		}

		if (str.equals(reversedString))
			return true;
		return false;
	}

	@GetMapping(path = "/countOccurences1")
	public int countOccurences1(String str, String search) {
		char searchingCharacter = search.toLowerCase().charAt(0);
		int occurrencies = 0;

		for (int i = 0; i < str.length(); i++) {
			if (str.toLowerCase().charAt(i) == searchingCharacter) {
				occurrencies++;
			}
		}

		return occurrencies;
	}

	@GetMapping(path = "/countOccurences2")
	public int countOccurences2(String str, String search) {
		char searchingCharacter = search.toLowerCase().charAt(0);
		int occurrencies = 0;

		String sub = str.toLowerCase().substring(0);
		int newIndex;
		do {
			newIndex = sub.indexOf(searchingCharacter);

			// Prevent going off the string
			if (newIndex + 1 < sub.length())
				sub = sub.toLowerCase().substring(newIndex + 1);
			else {
				if (newIndex >= 0)
					occurrencies++;
				break;
			}
			if (newIndex >= 0)
				occurrencies++;
		} while (newIndex >= 0);
		return occurrencies;
	}
}
