package com.spring.java.dto;

import java.util.HashMap;
import java.util.Map;

public class ReportDTO {
	Map<String, Integer> statisticheOperazioni = new HashMap<>();

	public ReportDTO() {}

	public ReportDTO(String operazione, int numeroVolte) {
		statisticheOperazioni.put(operazione, numeroVolte);
	}

	public ReportDTO(Map<String, Integer> statisticheOperazioni) {
		this.statisticheOperazioni = statisticheOperazioni;
	}

	public Map<String, Integer> getStatisticheOperazioni() {
		return statisticheOperazioni;
	}

	public void setStatisticheOperazioni(Map<String, Integer> statisticheOperazioni) {
		this.statisticheOperazioni = statisticheOperazioni;
	}

}
