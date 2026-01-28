package java2.interfacce.arcanoe;

import java.util.ArrayList;

public class Arca {
	private ArrayList<Animale> animaliSalvati;
	public Arca() {
		this.animaliSalvati =  new ArrayList<>();
	}
	
	public int getNumeroAnimali() {
		return animaliSalvati.size();
	}
	
	public void salva(Animale a) {
		if (animaliSalvati.indexOf(a) == -1)
			animaliSalvati.add(a);
		else
			throw new RuntimeException("L'animale è già presente sull'arca");
	}

	public String coro() {
		String res = "";

		for (Animale animale : animaliSalvati) {
			res += animale.verso() + "\n";
		}
		
		return res;
	}
	
	public String toString() {
		String res = "";

		for (Animale animale : animaliSalvati) {
			res += animale + "\n";
		}
		
		return res;
	}
}
