package java3.testing.testsEsempioStringa;

import static org.junit.Assert.*;

import org.junit.jupiter.api.Test;

import java3.testing.EsempioStringa;

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
		assertEquals("Il numero di occorrenze atteso", occ, es.contaOccorrenze(testo, "o"));
	}

	@Test
	void isPalindroma2() {
		EsempioStringa es = new EsempioStringa();
		String testo="osso";
		assertTrue(es.isPalindroma(testo));
	}

}
