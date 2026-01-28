package java3.testing.esercizi.tamagotchi;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

public class TestTamagotchi {
	private Tamagotchi t = new Tamagotchi("Kuma", "gATtO");

	// nome e specie assegnati correttamente peso, altezza, energia inizializzati ai valori previsti
	@Test
	public void testCostruttoreInizializzaValoriCorretti() {
		

		assertEquals("Kuma", t.getNome());
		assertEquals("Gatto", t.getSpecie());
		assertEquals(10.0, t.getAltezza(), 1e-15);
		assertEquals(100.0, t.getPeso(), 1e-15);
		assertEquals(3, t.getEnergia());
	}

	@Test
	public void testNomeNonModificabile() {
		String name = "Dusty";

		assertNotEquals(name, t.getNome());
	}

	@Test
	public void testSpecieNonModificabile() {
		String specie = "coniglio";

		assertNotEquals(specie, t.getSpecie());
	}

	@Test
	public void testMetodoMangia() {
		boolean mangia = t.mangia();

		assertTrue(mangia);
		assertEquals(4, t.getEnergia());
		assertEquals(11.0, t.getAltezza(), 1e-15);
		assertEquals(250.0, t.getPeso(), 1e-15);

		t.mangia();
		t.mangia();
		t.mangia();
		t.mangia();

		mangia = t.mangia();
		assertTrue(mangia);
		assertEquals(9, t.getEnergia());
	}

	@Test
	public void testGiocaEnergiaZero() {
		assertEquals(3, t.getEnergia());
		t.mangia();
		for(int i = 0; i < 5; i++)			
			t.gioca();
		
		assertFalse(t.gioca());
		assertEquals(0, t.getEnergia());

		t.gioca();

		assertEquals(0, t.getEnergia());
	}

	@Test
	public void testGiocaPesoMinimo() {
		assertEquals(100.0, t.getPeso(), 1e-15);
		
		assertFalse(t.gioca());
		assertEquals(3, t.getEnergia());
	}

	@Test
	public void testSequenzaOperazioni() {
		t.mangia();
		t.dorme();
		t.gioca();

		assertEquals(11.0, t.getAltezza(), 1e-15);
		assertEquals(250.0, t.getPeso(), 1e-15);
		assertEquals(4, t.getEnergia());
	}
}
