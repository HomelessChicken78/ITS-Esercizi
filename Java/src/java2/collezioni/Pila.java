package java2.collezioni;

import java.util.LinkedList;

import java2.eccezioni.MyExceptions.CollectionExceptions.ElementNotFoundException;

public class Pila<E> {
	private LinkedList<E> listaElementi= new LinkedList();

	public Pila() {
	}
	
	public void add(E obj) {
		listaElementi.addLast(obj);
	}
	
	public void remove() throws ElementNotFoundException{
		listaElementi.removeLast();
	}

	@Override
	public String toString() {
		return listaElementi.toString();
	}
}
