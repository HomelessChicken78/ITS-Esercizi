from classi import *
'''     
     
    Dalla vendita dei biglietti aerei, la compagnia aerea ITA ha guadagnato 12180.0 euro
'''
with open("report.txt", "w"):
    pass

# Sorry for the hardcoding with the writing in the documents. I don't see many other ways other than changing the "classi" module itself or using libraries
with open("report.txt", "a") as report:
      vc: VoloCommerciale = VoloCommerciale("COM123", 100)
           
      # vc: VoloCommerciale = VoloCommerciale("Altro", -2)
      print(f"Posti disponibili sul volo commerciale {vc.codice_volo()}:\n{vc.posti_disponibili()}")
      report.write(f"Posti disponibili sul volo commerciale {vc.codice_volo()}:\n{vc.posti_disponibili()}")
      vc.prenota_posto(70, "economica")
      report.write("\n70 posti prenotati su COM123 in classe economica.")
      print(f"{vc.posti_disponibili()}")
      report.write(f"\n{vc.posti_disponibili()}")
      vc.prenota_posto(20, "business")
      report.write("\n20 posti prenotati su COM123 in classe business.")
      print(f"{vc.posti_disponibili()}")
      report.write(f"\n{vc.posti_disponibili()}")
      vc.prenota_posto(70, "prima")
      report.write("\nNon è possibile riservare 70 posti in classe prima. Numero posti disponibili: 10")
      print(f"{vc.posti_disponibili()}")
      report.write(f"\n{vc.posti_disponibili()}")
      vc.prenota_posto(10, "prima")
      report.write("10 posti prenotati su COM123 in classe prima.")
      print(f"{vc.posti_disponibili()}")
      report.write(f"\n{vc.posti_disponibili()}")
      vc.prenota_posto(100, "economica")
      report.write("\nVolo COM123 al completo!")

      vch: VoloCharter = VoloCharter("CHA456", 200, 100)
      print(f"Posti disponibili sul volo charter {vch.codice_volo()}: {vch.max_posti()}")
      report.write(f"\nPosti disponibili sul volo charter {vch.codice_volo()}: {vch.max_posti()}")
      vch.prenota_posto()
      report.write("\nVolo charter CHA456 prenotato completamente per 20000.00€")
      vch.prenota_posto()
      report.write("\nIl volo charter CHA456 è gia prenotato.")

      vc2: VoloCommerciale = VoloCommerciale("COM456", 1000)
      vc2.prenota_posto(100, "economica")
      report.write("\n100 posti prenotati su COM456 in classe economica.")
      
      ita: CompagniaAerea = CompagniaAerea("ITA", 50.75)
      ita.aggiungi_volo(vc)
      ita.aggiungi_volo(vc2)
      ita.mostra_flotta()
      report.write("Ecco la flotta della compagnia aerea ITA:\nvolo commerciale COM123\nvolo commerciale COM456")
      ita.rimuovi_volo(vc2)
      ita.mostra_flotta()
      report.write("Ecco la flotta della compagnia aerea ITA:\nvolo commerciale COM123")
      ita.aggiungi_volo(vc2)
      print(f"Dalla vendita dei biglietti aerei, la compagnia aerea {ita.nome()} ha guadagnato {ita.guadagno()}€")
      report.write(f"\nDalla vendita dei biglietti aerei, la compagnia aerea {ita.nome()} ha guadagnato {ita.guadagno()}€")
