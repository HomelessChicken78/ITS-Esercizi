package com.rubrica.java.controller;

import java.util.List;

import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PatchMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
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
}
