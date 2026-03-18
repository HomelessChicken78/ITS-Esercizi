package com.spring.catalogo.service.scheduler;

import java.time.LocalDate;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.cloud.stream.function.StreamBridge;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Service;

import com.spring.catalogo.domains.StatoEvento;
import com.spring.catalogo.entity.EventOutbox;
import com.spring.catalogo.repository.RepositoryEventOutbox;

import jakarta.transaction.Transactional;


@Service
public class ServiceScheduler {
	@Autowired
	RepositoryEventOutbox outboxRepo;

	@Autowired
	StreamBridge streamBridge;

	@Scheduled(fixedDelay = 5000)
	@Transactional
	public void inviaMessaggi() {

		List<EventOutbox> eventi = outboxRepo.findPendingForUpdate();

		for (EventOutbox evento : eventi) {

			if (evento.getNumeroTentativi() > 5) {
				evento.setStatoEvento(StatoEvento.FAILED);
				outboxRepo.save(evento);
				continue;
			}

			try {
				if (streamBridge.send("productCatalog-out-0", evento.getPayload())) {
					evento.setStatoEvento(StatoEvento.SENT);
				} else {
	                evento.setStatoEvento(StatoEvento.FAILED);
	            }

				evento.setNumeroTentativi(evento.getNumeroTentativi() + 1);
			} catch (Exception e) {
				evento.setNumeroTentativi(evento.getNumeroTentativi() + 1);
			}

			evento.setDataUltimaModifica(LocalDate.now());
			outboxRepo.save(evento);
		}
	}
}