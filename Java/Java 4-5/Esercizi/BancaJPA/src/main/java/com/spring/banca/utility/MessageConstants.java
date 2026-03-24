package com.spring.banca.utility;

public class MessageConstants {
	private MessageConstants() {}

	public static String costruisciMsg404(String nomeEntita, Object id) {
		   return String.format("Non è stato possibile trovare un %s con id %s", 
		                        nomeEntita.toLowerCase(), 
		                        String.valueOf(id));
		}
}
