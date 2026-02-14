package com.spring.java.dao;

import java.util.List;

import com.spring.java.entity.Order;
import com.spring.java.entity.status.OrderStatus;

public interface OrderManager {
	public void insert(Order ord);
	
	public Order selectById(int idOrd);
	
	public List<Order> findAll();
	
	public Order delete(int idOrd);

	public void changeStatusById(int idOrd, OrderStatus newStatus);
}
