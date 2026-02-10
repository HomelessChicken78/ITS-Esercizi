package com.spring.lezioni.aop.interceptors;

import org.aspectj.lang.annotation.Around;
import org.aspectj.lang.annotation.Aspect;
import org.springframework.stereotype.Component;
import com.spring.lezioni.introduzione.CalcolatriceController;

import org.aspectj.lang.ProceedingJoinPoint;

@Component
@Aspect
public class SpettatoreAdvice {
	@Around("execution (* com.spring.lezioni.aop.entity.Artista.perform(..))")
	public void filtro(ProceedingJoinPoint jp) {
		// pre-processing
		System.out.println("gli spettatori prendono posto");
		System.out.println("gli spettatori spengono i cellulari");
		long start = System.currentTimeMillis();
		try {
			Thread.sleep(1000);
		} catch (InterruptedException e) {
			e.printStackTrace();
		}

		try {
			// chiamo il metodo target
		    jp.proceed();

		    // post-processing

		    // lo show è terminato con successo
		    System.out.println("applausi!!!!!!!!!!!!!!");
		    long end = System.currentTimeMillis();
		    System.out.println("lo show è durato " + (end - start) + " ms.");

		} catch (Throwable e) {
		    // post-processing con errore
			System.out.println("c'è stato un problema, show interrotto");
		}
	}
	
}
