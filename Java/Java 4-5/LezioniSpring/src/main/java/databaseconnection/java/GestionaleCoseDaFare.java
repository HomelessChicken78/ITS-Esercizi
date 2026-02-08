package databaseconnection.java;

import java.sql.*;
import java.util.Scanner;

public class GestionaleCoseDaFare {
	public static void main(String[] args) {
		// TodoDAO.inserisciTask("Primo Task");

		for (todoDTO td : TodoDAO.findAll())
			System.out.println(td);
		System.out.println("\n--------------------------------\n");

		Scanner sc = new Scanner(System.in);
		Scanner sc2 = new Scanner(System.in);
		int scelta = 0;
		do {
			System.out.print(
					"Inserisci un numero tra 0 e 2\n 0 = task da mettere come completo; 1 = aggiunge task; 2 = rimuove task\n");
			scelta = sc.nextInt();
		} while (scelta < 0 || scelta > 2);

		switch (scelta) {
		case 0:
			System.out.print("Inserisci l'id del nuovo task -> ");
			int todoId = sc2.nextInt();
			if (TodoDAO.setCompleted(todoId))
				System.out.println("Todo messo come completato con successo");
			else
				System.out.println("Non è stato possibile mettere il todo come completato");
			break;



		case 1:
			System.out.print("Inserisci il nome del nuovo task -> ");
			String taskName = sc2.nextLine();
			if (taskName.isBlank()) {
				System.out.println("Errore: Task non valido!");
				return;
			}
			boolean ok = TodoDAO.inserisciTask(taskName);

			if (ok)
				System.out.println("Task inserito correttamente!");
			else
				System.out.println("Task non salvato");
			break;



		case 2:
			System.out.print("Inserisci l'id del todo da rimuovere -> ");
			int taskId = sc2.nextInt();

			if (TodoDAO.rimuoviTask(taskId))
				System.out.println("Task rimosso correttamente!");
			else
				System.out.println("Task non rimosso");
			break;
		}
		
		sc.close();
		sc2.close();
	}
}
