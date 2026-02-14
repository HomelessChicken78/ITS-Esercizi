package com.spring.java.service;

import java.util.Collection;
import java.util.List;

import com.spring.java.dto.OrderCreateRequestDTO;
import com.spring.java.dto.OrderResponseDTO;

public interface OrderService {
	public OrderResponseDTO createOrder(OrderCreateRequestDTO ord);

	List<OrderResponseDTO> createListOrders(List<OrderCreateRequestDTO> listOrds);

	public OrderResponseDTO searchOrderById(int idOrd);

	public Collection<OrderResponseDTO> searchOrdersCreated();

	public Collection<OrderResponseDTO> searchOrdersConfirmed();

	public Collection<OrderResponseDTO> searchOrdersShipped();

	public OrderResponseDTO confirmOrder(int idOrder);

	public OrderResponseDTO shipOrder(int idOrder);

	public OrderResponseDTO deliverOrder(int idOrder);

	public OrderResponseDTO cancelOrder(int idOrder);
}