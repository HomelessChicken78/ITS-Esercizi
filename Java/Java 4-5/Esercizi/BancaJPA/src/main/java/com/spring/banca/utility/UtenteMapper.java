package com.spring.banca.utility;

import java.util.ArrayList;

import com.spring.banca.dto.UtenteConDatiSalienteDTO;
import com.spring.banca.dto.UtenteDTO;

public class UtenteMapper {
	private UtenteMapper() {}

	public static UtenteConDatiSalienteDTO toDatiSalienti(UtenteDTO dto) {
		if (dto == null)
            return null;

        UtenteConDatiSalienteDTO saliente = new UtenteConDatiSalienteDTO();
        
        saliente.setIdUtente(dto.getIdUtente());
        saliente.setNome(dto.getNome());
        saliente.setCognome(dto.getCognome());

        saliente.setListaConti(new ArrayList<>());

        return saliente;
	}

	public static UtenteDTO toDTO(Utent)
}
