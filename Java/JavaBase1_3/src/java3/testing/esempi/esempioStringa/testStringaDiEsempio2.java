package java3.testing.esempi.esempioStringa;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class testStringaDiEsempio2 {

	//@Test
	/* void test2() {
		fail("Not yet implemented");
	} */

	@Test
	void testContaOccorrenza2() {
		EsempioStringa es = new EsempioStringa();
		String testo="Giacomo sta facendo java e si diverte";
		int occ = 3;
		// Il numero di occorrenze atteso
		assertEquals(occ, es.contaOccorrenze(testo, "o"));
	}

	@Test
	void isPalindroma2() {
		EsempioStringa es = new EsempioStringa();
		String testo="osso";
		assertTrue(es.isPalindroma(testo));
	}

}
