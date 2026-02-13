package com.spring.java.entity;

import java.time.LocalDate;
import java.util.Objects;
import java.util.Set;
import java.util.TreeSet;

import com.spring.java.entity.status.OrderStatus;

public class Order {
	private int id;
	private Set<OrderItem> orderItemList;
	private double totalAmount;
	private OrderStatus status;
	private LocalDate createdAt;

	public Order() {
	}

	public Order(int id, Set<OrderItem> orderItemList, double totalAmount, OrderStatus status, LocalDate createdAt) {
		this.id = id;
		this.orderItemList = new TreeSet<>(orderItemList);
		this.totalAmount = totalAmount;
		this.status = status;
		this.createdAt = createdAt;
	}

	public int getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
	}

	public Set<OrderItem> getOrderItemList() {
		return new TreeSet<>(orderItemList);
	}

	public void setOrderItemList(Set<OrderItem> orderItemList) {
		this.orderItemList = new TreeSet<>(orderItemList);
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
		Order other = (Order) obj;
		return id == other.id;
	}

	@Override
	public String toString() {
		return id + " | " + totalAmount + "€ | " + status + " | created: " + createdAt;
	}
}
