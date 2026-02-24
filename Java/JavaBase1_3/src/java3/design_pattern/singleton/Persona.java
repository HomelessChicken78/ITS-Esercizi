package java3.design_pattern.singleton;

public class Persona {

    // Attributo necessario per far funzionare l'assegnazione nel costruttore
    private String nome;

    // 3. definisco un attributo statico per conservare quell'unica istanza che voglio fornire
    private static Persona sing;

    // 1. privatizzo il costruttore
    private Persona() {
        this.nome = "Nicol";
    }

    // 2. definisco un metodo statico (e pubblico) che torna l'oggetto Singleton
    public static Persona creaSingleton() {
        if (sing == null) {
            System.out.println("sto creando....");
            sing = new Persona();
            return sing;
        } else {
            return sing;
        }
    }
}