package java2.collezioni;

import java.util.LinkedList;
import java.util.NoSuchElementException;

public class Pila<E> {
	private LinkedList<E> listaElementi= new LinkedList();

	public Pila() {
	}
	
	public void add(E obj) {
		listaElementi.addLast(obj);
	}
	
	public void remove() throws NoSuchElementException{
		listaElementi.removeLast();
	}

	@Override
	public String toString() {
		return listaElementi.toString();
	}
}
