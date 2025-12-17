package java2.interfacce.esercizi.traghetto;

import java2.eccezioni.MyExceptions.CollectionExceptions.EmptyCollectionException;

public class CodaVuota extends EmptyCollectionException {

	public CodaVuota() {
	}

	public CodaVuota(String message) {
		super(message);
	}

	public CodaVuota(Throwable cause) {
		super(cause);
	}

	public CodaVuota(String message, Throwable cause) {
		super(message, cause);
	}

	public CodaVuota(String message, Throwable cause, boolean enableSuppression, boolean writableStackTrace) {
		super(message, cause, enableSuppression, writableStackTrace);
	}

}
