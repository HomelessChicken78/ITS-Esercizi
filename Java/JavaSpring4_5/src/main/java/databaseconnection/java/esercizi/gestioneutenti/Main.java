package databaseconnection.java.esercizi.gestioneutenti;

import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.Collection;
import java.util.Scanner;

public class Main {
	@SuppressWarnings("resource")
	public static void main(String[] args) {
		try {
			Connection dbUtenti = Database.getConnection();

			int scelta = 0;
			Scanner sc = new Scanner(System.in);

			do {
				System.out.println("Inserisci un numero tra 0 e 5");
				System.out.println("0 = Registra nuovo utente");
				System.out.println("1 = Login dell'utente");
				System.out.println("2 = Modifica password utente");
				System.out.println("3 = Cancella un utente attraverso username");
				System.out.println("4 = Visualizza tutti gli utenti (richiede password admin)");
				System.out.println("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=");
				scelta = sc.nextInt();
			} while (scelta < 0 || scelta > 4);

			switch (scelta) {
			case 0:
				System.out.println("===== REGISTRAZIONE UTENTE =====");
				System.out.print("Inserire il proprio nome -> "); String nome = new Scanner(System.in).nextLine();
				System.out.print("Inserire il proprio cognome -> "); String cognome = new Scanner(System.in).nextLine();
				System.out.print("Inserire una password: "); String password = new Scanner(System.in).nextLine();
				System.out.print("Inserire il proprio anno di nascita -> "); int annoNascita = new Scanner(System.in).nextInt();

				boolean usernameDisponibile = true;
				do {
					System.out.print("Inserire l'username -> "); String username = new Scanner(System.in).nextLine();

					try {
						DAOUtenti.registra(new Utente(nome, cognome, username, password, annoNascita));
						usernameDisponibile = true;
					} catch (UsernameGiaInUso e) {
						System.out.println("Errore! Username già in uso");
						usernameDisponibile = false;
					}
				} while (!usernameDisponibile);

				break;

			case 1:
				System.out.println("===== LOGIN UTENTE =====");
				try {
					System.out.print("Inserisci l'username -> "); String loginUsername = new Scanner(System.in).nextLine();
					System.out.print("Inserisci la password -> "); String loginPW = new Scanner(System.in).nextLine();
					Utente userLogged = DAOUtenti.login(loginUsername, loginPW);
					System.out.print(userLogged + " benvenuto!");
				} catch (CredenzialiErrate e) {
					System.out.println(e.getMessage());
				}
				break;

			case 2:
				System.out.println("===== MODIFICA PASSWORD =====");

				System.out.print("Inserisci l'username -> "); String usernameDaCambiarePW = new Scanner(System.in).nextLine();
				System.out.print("Inserisci la vecchia password: "); String vecchiaPassword = new Scanner(System.in).nextLine();
				System.out.print("Inserisci la nuova password: "); String nuovaPassword = new Scanner(System.in).nextLine();

				try {
					DAOUtenti.modificaPassword(usernameDaCambiarePW, vecchiaPassword, nuovaPassword);
				} catch (UsernameErrata e) {
					System.out.println(e.getMessage());
				} catch (CredenzialiErrate e) {
					System.out.println(e.getMessage());
				}
				
				break;

			case 3:
				System.out.println("===== CANCELLA UTENTE =====");
				System.out.print("Inserisci l'username -> "); String usernameDaCancellare = new Scanner(System.in).nextLine();

				try {
					DAOUtenti.cancellaUtente(usernameDaCancellare);
				} catch (UsernameErrata e) {
					System.out.println(e.getMessage());
				}
				break;

			case 4:
				System.out.println("===== VISUALIZZA UTENTI =====");

				Collection<Utente> res = DAOUtenti.listaUtenti();

				for (Utente ut : res) {
					System.out.println(ut);
				}
				break;

			default:
				throw new SQLException();
			}
		} catch (SQLException e) {
			e.printStackTrace();
		}
	}
}
