package com.spring.lezioni.prop;

import java.util.Locale;
import java.util.ResourceBundle;

public class Main {
	public static void main(String[] args) {
		// aggancio il properties
		ResourceBundle bundle = ResourceBundle.getBundle("com.spring.lezioni.prop.config");

		System.out.println(bundle.getString("name"));

		ResourceBundle bundle2 = ResourceBundle.getBundle("com.spring.lezioni.prop.hello", Locale.US);

		System.out.println(bundle2.getString("hello"));
	}
}
