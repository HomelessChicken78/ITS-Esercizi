package com.spring.java.dto;

import java.time.LocalDate;
import java.util.HashSet;
import java.util.Objects;
import java.util.Set;

import com.spring.java.entity.status.OrderStatus;

public class OrderResponseDTO {
	private Integer id;
	private Set<OrderItemDTO> orderItemList;
	private double totalAmount;
	private OrderStatus status;
	private LocalDate createdAt;

	public OrderResponseDTO() {
	}

	public OrderResponseDTO(int id, Set<OrderItemDTO> orderItemList, double totalAmount, OrderStatus status, LocalDate createdAt) {
		this.id = id;
		this.orderItemList = new HashSet<>(orderItemList);
		this.totalAmount = totalAmount;
		this.status = status;
		this.createdAt = createdAt;
	}

	public OrderResponseDTO(Set<OrderItemDTO> orderItemList) {
		this.id = null;
		this.orderItemList = new HashSet<>(orderItemList);
		this.totalAmount = orderItemList.stream().mapToDouble(it -> it.getUnitPrice() * it.getQuantity()).sum();
		this.status = OrderStatus.CREATED;
		this.createdAt = LocalDate.now();
	}

	public Integer getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
	}

	public Set<OrderItemDTO> getOrderItemList() {
		return new HashSet<>(orderItemList);
	}

	public void setOrderItemList(Set<OrderItemDTO> orderItemList) {
		this.orderItemList = new HashSet<>(orderItemList);
	}

	public double getTotalAmount() {
		return totalAmount;
	}

	public void setTotalAmount(double totalAmount) {
		this.totalAmount = totalAmount;
	}

	public OrderStatus getStatus() {
		return status;
	}

	public void setStatus(OrderStatus status) {
		this.status = status;
	}

	public LocalDate getCreatedAt() {
		return createdAt;
	}

	public void setCreatedAt(LocalDate createdAt) {
		this.createdAt = createdAt;
	}

	@Override
	public int hashCode() {
		return Objects.hash(id);
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		OrderResponseDTO other = (OrderResponseDTO) obj;
		return id == other.id;
	}

	@Override
	public String toString() {
		return id + " | " + totalAmount + "€ | " + status + " | created: " + createdAt;
	}
}
