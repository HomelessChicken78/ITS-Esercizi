package com.spring.java.service;

import java.util.Collection;

import com.spring.java.dto.OrderCreateRequestDTO;
import com.spring.java.dto.OrderResponseDTO;

public interface OrderService {
	public OrderResponseDTO createOrder(OrderCreateRequestDTO ord);

	public OrderResponseDTO searchOrderById(int idOrd);

	public Collection<OrderResponseDTO> searchOrdersCreated();

	public Collection<OrderResponseDTO> searchOrdersConfirmed();

	public Collection<OrderResponseDTO> searchOrdersShipped();

	public void confirmOrder(int idOrder);

	public void shipOrder(int idOrder);

	public void deliverOrder(int idOrder);

	public void cancelOrder(int idOrder);
}