package com.spring.java.dto;

import java.util.ArrayList;
import java.util.List;

public class OrderCreateRequestDTO {
	private List<OrderItemDTO> listOrderedProducts;

	public OrderCreateRequestDTO() {
	}

	public OrderCreateRequestDTO(List<OrderItemDTO> listOrderedProducts) {
		this.listOrderedProducts = new ArrayList<>(listOrderedProducts);
	}

	public List<OrderItemDTO> getListOrderedProducts() {
		return new ArrayList<>(listOrderedProducts);
	}

	public void setListOrderedProducts(List<OrderItemDTO> listOrderedProducts) {
		this.listOrderedProducts = new ArrayList<>(listOrderedProducts);
	}
}
