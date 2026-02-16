package com.spring.java.dao;

import java.util.HashMap;
import java.util.Map;

import org.springframework.stereotype.Repository;

@Repository
public class AdminsManagerImpl implements AdminsManager {
	private Map<String, String> mappa = new HashMap<>();

	public AdminsManagerImpl() {
		mappa.put("marco123", "password123");
		mappa.put("luca_89", "securePass456");
		mappa.put("giulia_98", "mySecret789");
		mappa.put("admin", "adminPass2023");
		mappa.put("anna_smith", "userPassword321");
		mappa.put("guest_user", "guestAccess000");
	}

	@Override
	public boolean authenticate(String username, String password) {
		return mappa.containsKey(username) && mappa.get(username).equals(password);
	}
}
