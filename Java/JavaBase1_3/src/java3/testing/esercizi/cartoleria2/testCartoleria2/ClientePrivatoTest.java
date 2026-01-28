package java3.testing.esercizi.cartoleria2.testCartoleria2;
import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

import java3.testing.esercizi.cartoleria2.Privato;

public class ClientePrivatoTest {
	Privato privato = new Privato("Nicol", 100.0);

	@Test
	public void testPagaHaSoldi() {
		privato.paga(90);
		assertEquals(10, privato.getCash());
	}

	@Test
	public void testPagaNonHaSoldi() {
		privato.paga(120);
		assertTrue(privato.getCash() > 0);
	}
}
