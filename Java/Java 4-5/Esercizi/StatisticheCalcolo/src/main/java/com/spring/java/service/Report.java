package com.spring.java.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.spring.java.dao.StatisticheFunzioni;
import com.spring.java.dto.ReportDTO;

@Service
public class Report {
	@Autowired
	StatisticheFunzioni stats;

	public ReportDTO frequenzaSingolaOperazione(String operation) {
		return new ReportDTO(operation, stats.select(operation));
	}

	public ReportDTO reportComplessivo() {
		return new ReportDTO(stats.selectAll());
	}
}
