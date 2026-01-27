package java3.testing.esempi.esempioStringa;

import static org.junit.Assert.*;

import org.junit.jupiter.api.Test;

class testStringaDiEsempio {

	//@Test
	/* void test() {
		fail("Not yet implemented");
	} */

	@Test
	void testContaOccorrenza() {
		EsempioStringa es = new EsempioStringa();
		String testo="Giacomo sta facendo java e si diverte";
		int occ = 3;
		assertEquals("Il numero di occorrenze atteso", occ, es.contaOccorrenze(testo, "o"));
	}

	@Test
	void isPalindroma() {
		EsempioStringa es = new EsempioStringa();
		String testo="osso";
		assertTrue(es.isPalindroma(testo));
	}

}
