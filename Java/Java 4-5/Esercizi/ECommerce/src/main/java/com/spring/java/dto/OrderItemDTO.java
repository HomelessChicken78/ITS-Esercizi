package com.spring.java.dto;

import java.util.Objects;

public class OrderItemDTO implements Comparable<OrderItemDTO> {
	private int productId, quantity;
	private double unitPrice;

	public OrderItemDTO() {
	}

	public OrderItemDTO(int productId, int quantity, double unitPrice) {
		this.productId = productId;
		this.quantity = quantity;
		this.unitPrice = unitPrice;
	}

	public int getProductId() {
		return productId;
	}

	public void setProductId(int productId) {
		this.productId = productId;
	}

	public int getQuantity() {
		return quantity;
	}

	public void setQuantity(int quantity) {
		this.quantity = quantity;
	}

	public double getUnitPrice() {
		return unitPrice;
	}

	public void setUnitPrice(double unitPrice) {
		this.unitPrice = unitPrice;
	}

	@Override
	public int hashCode() {
		return Objects.hash(productId);
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		OrderItemDTO other = (OrderItemDTO) obj;
		return productId == other.productId;
	}

	@Override
	public String toString() {
		return productId + " | quantity: " + quantity + " | " + unitPrice + "€";
	}

	@Override
	public int compareTo(OrderItemDTO other) {
		return Integer.compare(productId, other.getProductId());
	}
}

