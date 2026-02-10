package com.spring.java.interceptors;

import org.aspectj.lang.ProceedingJoinPoint;
import org.aspectj.lang.annotation.Around;
import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.annotation.Pointcut;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import com.spring.java.dao.StatisticheFunzioni;

@Component
@Aspect
public class InterceptorCalcolatrice {
	@Autowired
	StatisticheFunzioni dao;

	@Pointcut("execution(* com.spring.java.service.Calcolatrice.*(..))")
	public void operation() {}

	@Around("operation()")
	public int logging(ProceedingJoinPoint jp) throws Throwable {
		try {
			dao.increase(jp.getSignature().getName());
			int res = (int) jp.proceed();
			System.out.println("Risultato dell'operazione " + jp.getSignature().getName() + ": successo!");
			return res;
		} catch (ArithmeticException e) {
			System.out.println("Risultato dell'operazione " + jp.getSignature().getName() + ": errore!");
			return 0;
		}
	}
}
