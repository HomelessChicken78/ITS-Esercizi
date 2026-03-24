package com.spring.banca.entity;

import jakarta.persistence.*;
import lombok.*;

@Data
@AllArgsConstructor
@NoArgsConstructor
@Entity
public class Indirizzo {
	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private int idIndirizzo;

	@Column(nullable = false)
	private String via;

	@Column(nullable = false)
	private int cap;

	@Column(nullable = false)
	private String citta;

	@Column(nullable = false)
	private String provincia;
}
