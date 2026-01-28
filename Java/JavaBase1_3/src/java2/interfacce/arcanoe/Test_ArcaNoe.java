package java2.interfacce.arcanoe;

public class Test_ArcaNoe {
	public static void main(String[] args) {
		Arca arca = new Arca();
		
		Cane cane = new Cane();
		Gatto gatto = new Gatto();
		Coccodrillo giacomo = new Coccodrillo();
		Canarino titti = new Canarino();
		
		arca.salva(cane);
		arca.salva(gatto);
		arca.salva(giacomo);
		arca.salva(titti);
		
		System.out.println(arca);
		System.out.println(arca.coro());
		
		// arca.salva(titti);
	}
}
