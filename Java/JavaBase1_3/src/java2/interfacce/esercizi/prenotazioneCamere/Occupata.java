package java2.interfacce.esercizi.prenotazioneCamere;

import java2.eccezioni.MyExceptions.CollectionExceptions.DuplicateElementException;

public class Occupata extends DuplicateElementException {

	public Occupata() {
	}

	public Occupata(String message) {
		super(message);
	}

	public Occupata(Throwable cause) {
		super(cause);
	}

	public Occupata(String message, Throwable cause) {
		super(message, cause);
	}

	public Occupata(String message, Throwable cause, boolean enableSuppression, boolean writableStackTrace) {
		super(message, cause, enableSuppression, writableStackTrace);
	}

}
