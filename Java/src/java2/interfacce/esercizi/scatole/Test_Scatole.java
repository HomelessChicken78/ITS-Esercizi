package java2.interfacce.esercizi.scatole;

public class Test_Scatole {
	public static void main(String[] args) {
		Box grande = new Box(20, 30, 40);
		Box grande2 = new Box(30, 20, 40);
		Box piccola = new Box(10, 10, 50);
		Box piccola2 = new Box(10, 10, 30);
		System.out.println(grande.equals(grande2));  
		System.out.println(piccola.equals(piccola2));
		System.out.println(grande.getVolume());
		System.out.println(grande2.getVolume());
		System.out.println(piccola.getVolume());
		System.out.println(piccola2.getVolume());
		System.out.println(grande.compareTo(piccola));  // torna 1 -> ritorna 19000 per come funziona compareTo
		System.out.println(grande.compareTo(grande2));  // torna 0 >> stesso volume
		System.out.println("la piccola entra nella grande:" + piccola.fitsIn(grande));
		System.out.println("la piccola2 entra nella grande: " + piccola2.fitsIn(grande));		
	}
}
