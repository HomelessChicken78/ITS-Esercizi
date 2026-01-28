package java3.testing.esempi.esempioStringa;

import org.apache.logging.log4j.Logger;
import org.apache.logging.log4j.LogManager;

public class EsempioStringa {
	private static final Logger logger = LogManager.getLogger(EsempioStringa.class);

    public static void main(String[] args) {
        EsempioStringa es = new EsempioStringa();
        int oc = es.contaOccorrenze("Lorem ipsum test prova Cristiano", "r");
        logger.info("log4j Funziona e le occorrenze sono: " + oc);
        System.out.println(oc);
    }

    public boolean isPalindroma(String str1) {
        String str2 = ""; // puoi aggiungere un nuovo breakpoint qui e tracciare lo stato del programma da questo punto in poi

        for (int i = str1.length() - 1; i >= 0; i--) {
            str2 += str1.charAt(i);
        }

        return str1.equals(str2);
    }

    public int contaOccorrenze(String str1, String token) {
        int nOccorrenze = 0;

        for (int i = 0; i <= str1.length() - token.length(); i++) {
            String temp = str1.substring(i, i + token.length());
            if (temp.equals(token)) {
                nOccorrenze++;
            }
        }

        return nOccorrenze;
    }
}