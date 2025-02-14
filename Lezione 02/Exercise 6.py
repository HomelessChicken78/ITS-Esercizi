'''Exercise 6'''
ITS_Bakery_Menu={
    'Pizza': 9.00,
    'Pasta': 10.50,
    'Zuppa': 7.00,
    'Hamburger': 15.50,
    'Cotoletta': 10.00,
    'Salmone': 20.20,
    'Patatine Fritte': 5.50,
    'Patate al forno': 5.50,
    'Verdura del giorno': 7.00,
    'Cheesecake': 6.00,
    'Tiramisu': 6.00,
    'Focaccia con Nutella': 6.00,
    'Coca Cola': 3.50,
    'Acqua': 1.50,
    'Vino': 5.00,
}
ordine={
    'Zuppa' : ITS_Bakery_Menu['Zuppa'],
    'Cotoletta' :ITS_Bakery_Menu['Cotoletta'],
    'Patatine Fritte' : ITS_Bakery_Menu['Patatine Fritte'],
    'Acqua' : ITS_Bakery_Menu['Acqua'],
    'Cheesecake' : ITS_Bakery_Menu['Cheesecake']
}
print(ordine['Zuppa'] + ordine['Cotoletta'] + ordine['Patatine Fritte'] + ordine['Acqua'] + ordine['Cheesecake'], "€")