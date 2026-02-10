package com.spring.java.dao;

import java.util.HashMap;
import java.util.Map;

import org.springframework.stereotype.Repository;

@Repository
public class StatisticheFunzioni {
	Map<String, Integer> statistiche = new HashMap<>();

	public StatisticheFunzioni() {
		statistiche.put("add", 0);
		statistiche.put("subtract", 0);
		statistiche.put("multiply", 0);
		statistiche.put("divide", 0);
	}

	public int select(String operation) {
		return statistiche.get(operation);
	}

	public Map<String, Integer> selectAll() {
		return statistiche;
	}

	public boolean increase(String operation) {
		if (statistiche.containsKey(operation)) {
			statistiche.put(operation, statistiche.get(operation) + 1);
			return true;
		}

		return false;
	}
}
