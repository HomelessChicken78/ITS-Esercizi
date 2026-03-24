package com.spring.banca.entity;

import jakarta.persistence.*;
import lombok.*;

@Data
@AllArgsConstructor
@NoArgsConstructor
@Entity
public class Utente {
	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private int idUtente;

	@Column(nullable = false)
	private String nome;
	
	@Column(nullable = false)
	private String cognome;

	@Column(unique = true, nullable = false)
	private String mail;

	private String telefono;
}
