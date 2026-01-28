package java3.testing.esercizi.cartoleria2.testCartoleria2;
import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

import java3.testing.esercizi.cartoleria2.Azienda;

public class ClienteAziendaTest {
	Azienda az = new Azienda("Nicol", 100.0);

	@Test
	public void testPagaHaSoldi() {
		az.paga(90);
		assertEquals(1.0, az.getSaldoCc());
	}

	@Test
	public void testPagaNonHaSoldi() {
		az.paga(120);
		assertTrue(az.getSaldoCc() > 0);
	}
}
