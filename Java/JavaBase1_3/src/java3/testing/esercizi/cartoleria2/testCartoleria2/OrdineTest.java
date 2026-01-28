package java3.testing.esercizi.cartoleria2.testCartoleria2;

import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.ArgumentMatchers.anyDouble;
import static org.mockito.Mockito.verify;

import java.time.LocalDate;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.*;
import org.mockito.junit.jupiter.MockitoExtension;

import java3.testing.esercizi.cartoleria2.Cliente;
import java3.testing.esercizi.cartoleria2.Gomma;
import java3.testing.esercizi.cartoleria2.Ordine;
import java3.testing.esercizi.cartoleria2.Penna;


@ExtendWith(MockitoExtension.class)
public class OrdineTest {
	@Mock
	private Cliente client;

	@Mock
	private Penna penna1 = new Penna("Bic", "Model", 1.10, "blu");

	@Mock
	private Penna penna2 = new Penna("Stilo", "Cardio", 1.90, "black");

	@Mock
	private Gomma gomma1 = new Gomma("Rubber", "Reb", 2.2, "Round", 1.0);

	@InjectMocks
	private Ordine ord = new Ordine(LocalDate.now(), client);

	@Test
	public void chiudiTest() {
		// Arrange
		ord.carica(penna1);
		ord.carica(penna2);
		ord.carica(gomma1);

		// Act
		ord.chiudi();

		// Assert
		assertTrue(ord.isPagato());
		verify(client).paga(anyDouble());
		// verify(client).getAnagrafica();
	}
}
