package com.rubrica.java.service;

import java.util.List;

import com.rubrica.java.dao.DAORubrica;
import com.rubrica.java.dto.ContattoDTO;
import com.rubrica.java.dto.ElencoNomiProprietariAndNumeroTotaleProprietari;
import com.rubrica.java.dto.ProprietarioAndAnnoCreazioneRubrica;
import com.rubrica.java.dto.ProprietarioAndNumeroContatti;
import com.rubrica.java.dto.RubricaDTO;
import com.rubrica.java.entity.Contatto;
import com.rubrica.java.entity.Rubrica;

public class RubricaService {
	private DAORubrica dao = new DAORubrica();

	public static RubricaDTO RubricaEntity2DTO(Rubrica entity) {
		RubricaDTO dto = new RubricaDTO();

		if (entity != null) {
			dto.setId(entity.getId());
			dto.setProprietario(entity.getProprietario());
			dto.setAnnoCreazione(entity.getAnnoCreazione());

			for (Contatto contatto : entity.getListaContatti())
				dto.addContattoDTO(ContattoEntity2DTO(contatto));
		}

		return dto;
	}

	public static Rubrica RubricaDTO2Entity(RubricaDTO dto) {
		Rubrica entity = new Rubrica();

		if (dto != null) {
			entity.setId(dto.getId());
			entity.setProprietario(dto.getProprietario());
			entity.setAnnoCreazione(dto.getAnnoCreazione());

			for (ContattoDTO contattoDTO : dto.getListaContatti())
				entity.addContatto(ContattoDTO2Entity(contattoDTO));
		}

		return entity;
	}

	public static ContattoDTO ContattoEntity2DTO(Contatto entity) {
		ContattoDTO dto = new ContattoDTO();

		if (entity != null) {
			dto.setId(entity.getId());
			dto.setNome(entity.getNome());
			dto.setCognome(entity.getCognome());
			dto.setNumero(entity.getNumero());
			dto.setGruppoAppartenenza(entity.getGruppoAppartenenza());
			dto.setDataNascita(entity.getDataNascita());
			dto.setPreferito(entity.isPreferito());
		}

		return dto;
	}

	public static Contatto ContattoDTO2Entity(ContattoDTO dto) {
		Contatto entity = new Contatto();

		if (entity != null) {
			entity.setId(dto.getId());
			entity.setNome(dto.getNome());
			entity.setCognome(dto.getCognome());
			entity.setNumero(dto.getNumero());
			entity.setGruppoAppartenenza(dto.getGruppoAppartenenza());
			entity.setDataNascita(dto.getDataNascita());
			entity.setPreferito(dto.isPreferito());
		}

		return entity;
	}

	public boolean nuovaRubrica(RubricaDTO rubrica) {
		return dao.insert(RubricaDTO2Entity(rubrica));
	}

	public RubricaDTO visualizzaRubricaPerId(int idRubrica) {
		return RubricaEntity2DTO(dao.cercaPerId(idRubrica));
	}

	public List<RubricaDTO> visualizzaTutteRubriche() {
		return dao.visualizzaTutti()
				.stream()
				.map(entity -> RubricaEntity2DTO(entity))
				.toList();
	}

	public RubricaDTO cancellaRubrica(int idRubrica) {
		return RubricaEntity2DTO(dao.cancella(idRubrica));
	}

	public ProprietarioAndAnnoCreazioneRubrica propietarioAndAnnoCreazione(int idRubrica) {
		Rubrica res = dao.cercaPerId(idRubrica);

		return new ProprietarioAndAnnoCreazioneRubrica(res.getProprietario(), res.getAnnoCreazione());
	}

	public RubricaDTO modificaProprietario(int idRubrica, String nuovoProprietario) {
		Rubrica rubricaDaAggiornare = dao.cercaPerId(idRubrica);
		dao.cancella(idRubrica);
		rubricaDaAggiornare.setProprietario(nuovoProprietario);
		dao.insert(rubricaDaAggiornare);

		return RubricaEntity2DTO(rubricaDaAggiornare);
	}

	public RubricaDTO modificaAnnoCreazione(int idRubrica, int annoCreazione) {
		Rubrica rubricaDaAggiornare = dao.cercaPerId(idRubrica);
		dao.cancella(idRubrica);
		rubricaDaAggiornare.setAnnoCreazione(annoCreazione);
		dao.insert(rubricaDaAggiornare);

		return RubricaEntity2DTO(rubricaDaAggiornare);
	}

	public ElencoNomiProprietariAndNumeroTotaleProprietari nomiProprietariAndNumero() {
		List<String> elenco = dao.visualizzaTutti()
				.stream()
				.map(r -> r.getProprietario().toLowerCase())
				.distinct()
				.toList();
		int numero = elenco.size();

		return new ElencoNomiProprietariAndNumeroTotaleProprietari(elenco, numero);
	}

	public ProprietarioAndAnnoCreazioneRubrica piuVecchia() {
		Rubrica res = dao.visualizzaTutti()
				.stream()
				.sorted((r1, r2) -> Integer.compare(r1.getAnnoCreazione(), r2.getAnnoCreazione()))
				.findFirst().orElse(null);

		return new ProprietarioAndAnnoCreazioneRubrica(res.getProprietario(), res.getAnnoCreazione());
	}

	public List<Integer> listaAnniCreazione() {
		return dao.visualizzaTutti()
				.stream()
				.map(r -> r.getAnnoCreazione())
				.sorted((y1, y2) -> Integer.compare(y1, y2))
				.distinct()
				.toList();
	}

	
	public ProprietarioAndNumeroContatti statisticheRubrica(int idRubrica) {
		RubricaDTO rubrica = visualizzaRubricaPerId(idRubrica);

		if (rubrica != null)
			return new ProprietarioAndNumeroContatti(rubrica.getProprietario(), rubrica.getListaContatti().size());

		return null;
	}

	public boolean nuovoContatto(int idRubrica, ContattoDTO contatto) {
		return dao.cercaPerId(idRubrica).addContatto(ContattoDTO2Entity(contatto));
	}

	public ContattoDTO visualizzaContattoPerId(int idRubrica, int idContatto) {
		RubricaDTO rubrica = visualizzaRubricaPerId(idRubrica);

		if (rubrica != null)
			return
				rubrica.getListaContatti()
				.stream()
				.filter(c -> c.getId() == idContatto)
				.findAny().orElse(null);

		return null;
	}

	public ContattoDTO modicaContatto(int idRubrica, int idContatto, ContattoDTO contattoAggiornato) {
		contattoAggiornato.setId(idContatto);
		cancellaContatto(idRubrica, idContatto);
		nuovoContatto(idRubrica, contattoAggiornato);

		return contattoAggiornato;
	}

	public ContattoDTO cancellaContatto(int idRubrica, int idContatto) {
		Rubrica rubrica = dao.cercaPerId(idRubrica);

		if (rubrica != null)
			return ContattoEntity2DTO(rubrica.removeContatto(idContatto));

		return null;
	}

	public List<ContattoDTO> visualizzaTuttiContatti(int idRubrica) {
		RubricaDTO rubrica = visualizzaRubricaPerId(idRubrica);

		if (rubrica != null)
			return rubrica.getListaContatti();

		return null;
	}

	public int visualizzaNumeroContatti(int idRubrica) {
		RubricaDTO rubrica = visualizzaRubricaPerId(idRubrica);

		if (rubrica != null)
			return rubrica.getListaContatti().size();

		return 0;
	}

	public ContattoDTO visualizzaContattoPerNumero(int idRubrica, String numero) {
		RubricaDTO rubrica = visualizzaRubricaPerId(idRubrica);

		if (rubrica != null)
			return
				rubrica.getListaContatti()
				.stream()
				.filter(c -> c.getNumero().equals(numero))
				.findFirst().orElse(null);

		return null;
	}

	public List<String> nomeAndCognomeContattiDiUnGruppo(int idRubrica, String gruppo) {
		RubricaDTO rubrica = visualizzaRubricaPerId(idRubrica);

		if (rubrica != null)
			return
				rubrica.getListaContatti()
				.stream()
				.filter(c -> c.getGruppoAppartenenza().equals(gruppo))
				.map(c -> c.getNome() + " " + c.getCognome())
				.toList();

		return null;
	}

	public int numeroContattiGruppo(int idRubrica, String gruppo) {
		RubricaDTO rubrica = visualizzaRubricaPerId(idRubrica);

		if (rubrica != null) {
			List<String> res = nomeAndCognomeContattiDiUnGruppo(idRubrica, gruppo);

			if (res != null && res.size() > 0)
				return res.size();
		}

		return 0;
	}

	public void cancellaGruppo(int idRubrica, String gruppo) {
		Rubrica rubrica = dao.cercaPerId(idRubrica);

		if (rubrica != null)
			rubrica.getListaContatti()
				.stream()
				.filter(c -> c.getGruppoAppartenenza().equals(gruppo))
				.forEach(c -> cancellaContatto(idRubrica, c.getId()));
	}

	public boolean mettiPreferito(int idRubrica, int idContatto) {
		if (visualizzaContattoPerId(idRubrica, idContatto) != null) {
			Contatto trovato = dao.cercaPerId(idRubrica).getListaContatti()
			.stream()
			.filter(c -> c.getId() == idContatto)
			.findAny().orElse(null);

			if (trovato != null) {
				trovato.setPreferito(true);
				return true;
			}
		}

		return false;
	}

	public List<ContattoDTO> visualizzaPreferiti(int idRubrica) {
		RubricaDTO rubrica = visualizzaRubricaPerId(idRubrica);

		if (rubrica != null)
			return
				rubrica.getListaContatti()
				.stream()
				.filter(c -> c.isPreferito())
				.toList();

		return null;
	}
}
