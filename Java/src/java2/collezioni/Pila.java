package java2.collezioni;

import java.util.LinkedList;

public class Pila<E> {
	private LinkedList<E> listaElementi= new LinkedList();

	public Pila() {
	}
	
	public void add(E obj) {
		listaElementi.addLast(obj);
	}
	
	public void remove() {
		listaElementi.removeLast();
	}

	@Override
	public String toString() {
		return listaElementi.toString();
	}
}
