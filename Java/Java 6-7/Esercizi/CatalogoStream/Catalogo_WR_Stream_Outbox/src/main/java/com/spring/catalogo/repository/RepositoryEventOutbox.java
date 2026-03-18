package com.spring.catalogo.repository;

import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;

import com.spring.catalogo.entity.EventOutbox;

public interface RepositoryEventOutbox extends JpaRepository<EventOutbox, Integer> {
	@Query(value = "SELECT * FROM event_outbox WHERE stato = 'PENDING' FOR UPDATE", nativeQuery = true)
	  List<EventOutbox> findPendingForUpdate();
}
