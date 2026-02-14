package com.spring.java.dao;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.springframework.stereotype.Repository;

import com.spring.java.entity.Order;
import com.spring.java.entity.status.OrderStatus;
import com.spring.java.exception.DuplicateIDException;
import com.spring.java.exception.OrderNotFoundException;

@Repository
public class OrderManagerImpl implements OrderManager {
	private Map<Integer, Order> mappa = new HashMap<>();
	private int serial = 0;

	@Override
	public synchronized void insert(Order ord) {
		if(mappa.containsKey(ord.getId()))
			throw new DuplicateIDException("Already exists an order with ID " + ord.getId());

		if (ord.getId() == null)
			ord.setId(serial);

		if (ord.getId() != null && ord.getId() > serial)
			serial = ord.getId();
		serial++;

		mappa.put(ord.getId(), ord);
	}

	@Override
	public Order selectById(int idOrd) {
		if(!mappa.containsKey(idOrd))
			throw new OrderNotFoundException("Could not find order with ID " + idOrd);

		return mappa.get(idOrd);
	}

	@Override
	public List<Order> findAll(){
		return new ArrayList<Order>(mappa.values());
	}

	@Override
	public Order delete(int idOrd) {
		if(!mappa.containsKey(idOrd))
			throw new OrderNotFoundException("Could not find order with ID " + idOrd);

		return mappa.remove(idOrd);
	}

	@Override
	public void changeStatusById(int idOrd, OrderStatus newStatus) {
		selectById(idOrd).setStatus(newStatus);
	}
}