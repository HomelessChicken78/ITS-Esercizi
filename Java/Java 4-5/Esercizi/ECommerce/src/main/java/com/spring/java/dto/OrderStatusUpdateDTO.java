package com.spring.java.dto;

import com.spring.java.entity.status.OrderStatus;

public class OrderStatusUpdateDTO {
	private OrderStatus status;

	public OrderStatusUpdateDTO() {}

	public OrderStatusUpdateDTO(OrderStatus status) {
		this.status = status;
	}

	public OrderStatus getStatus() {
		return status;
	}

	public void setStatus(OrderStatus status) {
		this.status = status;
	}
}
