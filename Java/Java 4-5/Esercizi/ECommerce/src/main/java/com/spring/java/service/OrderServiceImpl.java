package com.spring.java.service;

import java.util.ArrayList;
import java.util.Collection;
import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;

import com.spring.java.dao.OrderManager;
import com.spring.java.dao.ProductManager;
import com.spring.java.dto.OrderCreateRequestDTO;
import com.spring.java.dto.OrderItemDTO;
import com.spring.java.dto.OrderResponseDTO;
import com.spring.java.entity.Order;
import com.spring.java.entity.OrderItem;
import com.spring.java.entity.Product;
import com.spring.java.exception.InsufficientStockException;
import com.spring.java.exception.ProductNotFoundException;

@Repository
public class OrderServiceImpl implements OrderService {
	@Autowired
	OrderManager dao;

	@Autowired
	ProductManager prods;

	public static OrderResponseDTO orderEntity2DTO(Order entity) {
		if (entity == null)
			return null;

		OrderResponseDTO dto = new OrderResponseDTO();
		dto.setId(entity.getId());
		dto.setTotalAmount(entity.getTotalAmount());
		dto.setStatus(entity.getStatus());
		dto.setCreatedAt(entity.getCreatedAt());
		dto.setOrderItemList(entity.getOrderItemList().stream().map(ent -> itemEntity2DTO(ent)).collect(Collectors.toSet()));

		return dto;
	}

	public static Order orderDTO2Entity(OrderResponseDTO dto) {
	    if (dto == null)
	        return null;

	    Order entity = new Order();
	    entity.setId(dto.getId());
	    entity.setTotalAmount(dto.getTotalAmount());
	    entity.setStatus(dto.getStatus());
	    entity.setCreatedAt(dto.getCreatedAt());
	    
	    if (dto.getOrderItemList() != null) {
	        entity.setOrderItemList(dto.getOrderItemList().stream()
	            .map(d -> itemDTO2Entity(d))
	            .collect(Collectors.toSet()));
	    }

	    return entity;
	}

	public static OrderItemDTO itemEntity2DTO(OrderItem entity) {
		if (entity == null)
			return null;

		OrderItemDTO dto = new OrderItemDTO();
		dto.setProductId(entity.getProductId());
		dto.setQuantity(entity.getQuantity());
		dto.setUnitPrice(entity.getUnitPrice());

		return dto;
	}

	public static OrderItem itemDTO2Entity(OrderItemDTO dto) {
	    if (dto == null)
	        return null;

	    OrderItem entity = new OrderItem();
	    entity.setProductId(dto.getProductId());
	    entity.setQuantity(dto.getQuantity());
	    entity.setUnitPrice(dto.getUnitPrice());

	    return entity;
	}

	@Override
	public OrderResponseDTO createOrder(OrderCreateRequestDTO ord) {
		Set<OrderItem> setOrderItems = ord.getListOrderedProducts().stream().map(d -> itemDTO2Entity(d)).collect(Collectors.toSet());

		for (OrderItem ordered : setOrderItems) {
			Product prod = prods.selectById(ordered.getProductId());

			if (prod == null)
				throw new ProductNotFoundException();

			if (prod.getStock() < ordered.getQuantity())
				throw new InsufficientStockException();

			ordered.setUnitPrice(prod.getPrice());
		}

		Order newOrder = new Order(setOrderItems);
		dao.insert(newOrder);
		return orderEntity2DTO(newOrder);
	}

	public List<OrderResponseDTO> createListOrders(List<OrderCreateRequestDTO> listOrds) {
		List<OrderResponseDTO> res = new ArrayList<>();

		for (OrderCreateRequestDTO ord : listOrds)
			res.add(createOrder(ord));

		return res;
	}

	@Override
	public OrderResponseDTO searchOrderById(int idOrd) {
		// TODO Auto-generated method stub
		return null;
	}

	@Override
	public Collection<OrderResponseDTO> searchOrdersCreated() {
		// TODO Auto-generated method stub
		return null;
	}

	@Override
	public Collection<OrderResponseDTO> searchOrdersConfirmed() {
		// TODO Auto-generated method stub
		return null;
	}

	@Override
	public Collection<OrderResponseDTO> searchOrdersShipped() {
		// TODO Auto-generated method stub
		return null;
	}

	@Override
	public void confirmOrder(int idOrder) {
		// TODO Auto-generated method stub

	}

	@Override
	public void shipOrder(int idOrder) {
		// TODO Auto-generated method stub

	}

	@Override
	public void deliverOrder(int idOrder) {
		// TODO Auto-generated method stub

	}

	@Override
	public void cancelOrder(int idOrder) {
		// TODO Auto-generated method stub

	}

}
