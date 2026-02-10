package com.rubrica.java.controller;

import java.util.List;

import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PatchMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import com.rubrica.java.dto.ContattoDTO;
import com.rubrica.java.dto.ElencoNomiProprietariAndNumeroTotaleProprietari;
import com.rubrica.java.dto.ProprietarioAndAnnoCreazioneRubrica;
import com.rubrica.java.dto.ProprietarioAndNumeroContatti;
import com.rubrica.java.dto.RubricaDTO;
import com.rubrica.java.service.RubricaService;

@RestController
@RequestMapping(path = "/rubriche")
public class RubricaController {	
	private RubricaService service = new RubricaService();

	@PostMapping(consumes = "application/json")
	public boolean aggiungiRubrica(@RequestBody RubricaDTO rubrica) {
		return service.nuovaRubrica(rubrica);
	}

	@GetMapping(path = "/{idRubrica}", produces = "application/json")
	public RubricaDTO cercaPerId(@PathVariable int idRubrica) {
		return service.visualizzaRubricaPerId(idRubrica);
	}

	@GetMapping(produces = "application/json")
	public List<RubricaDTO> visualizzaTutteRubriche() {
		return service.visualizzaTutteRubriche();
	}

	@DeleteMapping(path = "/{idRubrica}", produces = "application/json")
	public RubricaDTO cancellaRubrica(@PathVariable int idRubrica) {
		return service.cancellaRubrica(idRubrica);
	}

	@GetMapping(path = "/{idRubrica}/proprietariEAnni", produces = "application/json")
	public ProprietarioAndAnnoCreazioneRubrica propietarioAndAnnoCreazione(@PathVariable int idRubrica) {
		return service.propietarioAndAnnoCreazione(idRubrica);
	}

	@PatchMapping(path = "/{idRubrica}/proprietario", produces = "application/json")
	public RubricaDTO modificaProprietario(@PathVariable int idRubrica, String proprietario) {
		return service.modificaProprietario(idRubrica, proprietario);
	}

	@PatchMapping(path = "/{idRubrica}/annoCreazione", produces = "application/json")
	public RubricaDTO modificaAnnoCreazione(@PathVariable int idRubrica, int anno) {
		return service.modificaAnnoCreazione(idRubrica, anno);
	}

	@GetMapping(path = "/nomiENumeroProprietari", produces = "application/json")
	public ElencoNomiProprietariAndNumeroTotaleProprietari nomiENumeroProprietari() {
		return service.nomiProprietariAndNumero();
	}

	@GetMapping(path = "/piuVecchia", produces = "application/json")
	public ProprietarioAndAnnoCreazioneRubrica cercaRubricaPiuVecchia() {
		return service.piuVecchia();
	}

	@GetMapping(path =  "/anniCreazione", produces = "application/json")
	public List<Integer> listaAnniCreazione() {
		return service.listaAnniCreazione();
	}

	@GetMapping(path = "/{idRubrica}/proprietarioENumeroContatti", produces = "application/json")
	public ProprietarioAndNumeroContatti proprietarioENumeroContatti(@PathVariable int idRubrica) {
		return service.statisticheRubrica(idRubrica);
	}

	@PostMapping(path = "/{idRubrica}/contatti", consumes = "application/json")
	public boolean aggiungiContatto(@PathVariable int idRubrica, @RequestBody ContattoDTO contatto) {
		return service.nuovoContatto(idRubrica, contatto);
	}

	@GetMapping(path = "/{idRubrica}/contatti/{idContatto}", produces = "application/json")
	public ContattoDTO cercaContattoPerId(@PathVariable int idRubrica, @PathVariable int idContatto) {
		return service.visualizzaContattoPerId(idRubrica, idContatto);
	}

	@PutMapping(path = "/{idRubrica}/contatti/{idContatto}", consumes = "application/json", produces = "application/json")
	public ContattoDTO modificaContatto(@PathVariable int idRubrica, @PathVariable int idContatto, @RequestBody ContattoDTO contatto) {
		return service.modicaContatto(idRubrica, idContatto, contatto);
	}

	@DeleteMapping(path = "/{idRubrica}/contatti/{idContatto}", produces = "application/json")
	public ContattoDTO cancellaContatto(@PathVariable int idRubrica, @PathVariable int idContatto) {
		return service.cancellaContatto(idRubrica, idContatto);
	}

	@GetMapping(path = "/{idRubrica}/contatti")
	public List<ContattoDTO> visualizzaTuttiContatti(@PathVariable int idRubrica) {
		return service.visualizzaTuttiContatti(idRubrica);
	}

	@GetMapping(path = "/{idRubrica}/contatti/numero")
	public int visualizzaNumeroContatti(@PathVariable int idRubrica) {
		return service.visualizzaNumeroContatti(idRubrica);
	}

	@GetMapping(path = "/{idRubrica}/contatti/cercaNumero", produces = "application/json")
	public ContattoDTO cercaContattoPerNumero(@PathVariable int idRubrica, String numero) {
		return service.visualizzaContattoPerNumero(idRubrica, numero);
	}

	@GetMapping(path = "/{idRubrica}/gruppi/{nomeGruppo}", produces = "application/json")
	public List<String> nomeAndCognomeContattiDiUnGruppo(@PathVariable int idRubrica, @PathVariable String nomeGruppo) {
		return service.nomeAndCognomeContattiDiUnGruppo(idRubrica, nomeGruppo);
	}

	@GetMapping(path = "/{idRubrica}/gruppi/{nomeGruppo}/numero")
	public int numeroContattiGruppo(@PathVariable int idRubrica, @PathVariable String nomeGruppo) {
		return service.numeroContattiGruppo(idRubrica, nomeGruppo);
	}

	@DeleteMapping(path = "/{idRubrica}/gruppi/{nomeGruppo}")
	public void cancellaGruppo(@PathVariable int idRubrica, @PathVariable String nomeGruppo) {
		service.cancellaGruppo(idRubrica, nomeGruppo);
	}

	@PatchMapping(path = "/{idRubrica}/contatti/{idContatto}")
	public boolean mettiPreferito(@PathVariable int idRubrica, @PathVariable int idContatto) {
		return service.mettiPreferito(idRubrica, idContatto);
	}

	@GetMapping(path = "/{idRubrica}/contatti/preferiti", produces = "application/json")
	public List<ContattoDTO> visualizzaPreferiti(@PathVariable int idRubrica) {
		return service.visualizzaPreferiti(idRubrica);
	}
}
