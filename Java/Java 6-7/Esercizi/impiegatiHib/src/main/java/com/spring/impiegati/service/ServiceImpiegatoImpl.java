package com.spring.impiegati.service;

import java.time.LocalDate;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import com.spring.impiegati.dto.ImpiegatoDTO;
import com.spring.impiegati.dto.NomeAndCognomeImpiegatoDTO;
import com.spring.impiegati.dto.TotaleSalariDTO;
import com.spring.impiegati.entity.Impiegato;
import com.spring.impiegati.exception.DuplicateIDException;
import com.spring.impiegati.exception.NotFoundException;

import static com.spring.impiegati.mapper.Mapper.*;
import com.spring.impiegati.repository.RepositoryImpiegati;

import jakarta.transaction.Transactional;

@Service
@Transactional
public class ServiceImpiegatoImpl implements ServiceImpiegato {
	@Autowired
	RepositoryImpiegati dao;

	@Override
	public void assumi(ImpiegatoDTO impiegato) {
		if (dao.save(DTO2Entity(impiegato)) == null)
			throw new DuplicateIDException("Esiste già un impiegato con matricola " + impiegato.getMatricola());
	}

	@Override
	public ImpiegatoDTO cercaPerMatricola(String matricola) {
		return entity2DTO(dao.findById(matricola).orElseThrow(() -> new NotFoundException("Non esiste un impiegato con matricola: " + matricola)));
	}

	@Override
	public List<ImpiegatoDTO> visualizzaTutti() {
		return dao.findAll()
				.stream()
				.map(imp -> entity2DTO(imp))
				.toList();
	}

	@Override
	public ImpiegatoDTO cancellaPerMatricola(String matricola) {
		Impiegato impiegatoTrovato = dao.findById(matricola).orElseThrow(() -> new NotFoundException("Non esiste un impiegato con matricola: " + matricola));
		ImpiegatoDTO daRitornare = entity2DTO(impiegatoTrovato);

		dao.delete(impiegatoTrovato);
		return daRitornare;
	}

	@Override
	public ImpiegatoDTO modificaSalario(String matricola, double nuovoSalario) {
		if (nuovoSalario < 0)
			throw new SalarioInvalidoException("Il salario non può essere un numero inferiore a 0");
		Impiegato impiegatoTrovato = dao.findById(matricola).orElseThrow(() -> new NotFoundException("Non esiste un impiegato con matricola: " + matricola));

		impiegatoTrovato.setSalarioMensile(nuovoSalario);

		return entity2DTO(impiegatoTrovato);
	}

	@Override
	public NomeAndCognomeImpiegatoDTO eliminaPerMatricola(String matricola) {
		ImpiegatoDTO impiegatoCancellato = cancellaPerMatricola(matricola);

		return new NomeAndCognomeImpiegatoDTO(
				impiegatoCancellato.getNome(),
				impiegatoCancellato.getCognome()
			);
	}

	@Override
	public List<NomeAndCognomeImpiegatoDTO> nomiAndCognomiOrdinatiPerMatricola() {
		return dao.findAll()
				.stream()
				.sorted((imp1, imp2) -> imp1.getMatricola().compareTo(imp2.getMatricola()))
				.map(imp -> new NomeAndCognomeImpiegatoDTO(imp.getNome(), imp.getCognome()))
				.toList();
	}

	@Override
	public TotaleSalariDTO totaleSalariPagato() {
		double res = dao.findAll()
				.stream()
				.mapToDouble(imp -> imp.getSalarioMensile())
				.sum();

		return new TotaleSalariDTO(res);
	}

	@Override
	public List<ImpiegatoDTO> impiegatiOrdinatiPerCognome() {
		return dao.findAll()
				.stream()
				.sorted((imp1, imp2) -> imp1.getCognome().compareTo(imp2.getCognome()))
				.map(imp -> entity2DTO(imp))
				.toList();
	}

	@Override
	public ImpiegatoDTO assuntoDaPiuTempo() {
		return entity2DTO(dao.findAll()
				.stream()
				.sorted((imp1, imp2) -> imp1.getDataAssunzione().compareTo(imp2.getDataAssunzione()))
				.findFirst()
				.orElse(null));
	}

	@Override
	public ImpiegatoDTO salarioMaggioreDopoData(LocalDate data) {
		return entity2DTO(dao.findAll()
				.stream()
				.filter(imp -> imp.getDataAssunzione().isAfter(data))
				.sorted((imp1, imp2) -> Double.compare(imp2.getSalarioMensile(), imp1.getSalarioMensile()))
				.findFirst()
				.orElse(null));
	}
}
