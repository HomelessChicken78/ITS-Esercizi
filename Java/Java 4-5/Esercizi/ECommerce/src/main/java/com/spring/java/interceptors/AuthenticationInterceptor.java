package com.spring.java.interceptors;

import javax.security.sasl.AuthenticationException;

import org.aspectj.lang.ProceedingJoinPoint;
import org.aspectj.lang.annotation.Around;
import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.annotation.Before;
import org.aspectj.lang.annotation.Pointcut;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import com.spring.java.dao.AdminsManager;
import com.spring.java.dto.ProductAndCredentialsDTO;

@Component
@Aspect
public class AuthenticationInterceptor {
	@Autowired
	AdminsManager dao;

	@Pointcut("execution(* com.spring.java.service.ProductService.*(..))")
	public void operation() {
	}

	@Around("operation()")
	public void authenticate(ProceedingJoinPoint jp) throws Throwable {
		Object[] args = jp.getArgs();

		ProductAndCredentialsDTO credentials = null;
		for (Object arg : args) {
			if (arg instanceof ProductAndCredentialsDTO) {
				credentials = (ProductAndCredentialsDTO) arg;
				break;
			}
		}

		if (credentials != null)
			 if (dao.authenticate(credentials.getUsername(), credentials.getPassword()))
				 jp.proceed();
			 else
				 throw new AuthenticationException("Unauthorized");
		else
			jp.proceed();
	}
}
