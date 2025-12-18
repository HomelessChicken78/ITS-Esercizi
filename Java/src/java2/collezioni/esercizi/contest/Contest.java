package java2.collezioni.esercizi.contest;

import java.util.LinkedList;

import java2.eccezioni.MyExceptions.CollectionExceptions.ElementNotFoundException;

public class Contest {
	private LinkedList<Performer> listaArtisti = new LinkedList<>();

	public Contest() {
	}

	public LinkedList<Performer> getListaArtisti() {
		return new LinkedList<>(listaArtisti);
	}

	public void signUp(Performer performer) throws PerformerDuplicatoException {
		if (listaArtisti.contains(performer))
			throw new PerformerDuplicatoException("L'artista è già parte del contest!");
		listaArtisti.addLast(performer);
	}
	
	public void registerVoteFor(Performer performer) throws ElementNotFoundException {
		if (!listaArtisti.contains(performer))
			throw new ElementNotFoundException("L'artista non è nel contest!");
		performer.incrementaVoto(1);
	}
	
	public Performer getWinner() {
		if (listaArtisti.size() == 0)
			return null;
		
		Performer highestVoto = listaArtisti.get(0);
		
		for (Performer performer : listaArtisti) {
			if (performer.compareTo(highestVoto) > 0)
				highestVoto = performer;
		}
		
		return highestVoto;
	}

	@Override
	public String toString() {
		return listaArtisti.toString();
	}
	
	
}
