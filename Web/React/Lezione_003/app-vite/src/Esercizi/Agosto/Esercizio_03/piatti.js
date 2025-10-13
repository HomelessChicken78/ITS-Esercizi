function Piatto(id, nome, prezzo) {
    this.id = id;
    this.nome = nome;
    this.prezzo = prezzo;
}

const piatti = [
    new Piatto(0, "Pasta al sugo", 7.00), new Piatto(1, "Pasta al pesto", 7.00), new Piatto(2, "Carbonara", 12.00),
    new Piatto(3, "Amatriciana", 12.00), new Piatto(4, "Pasta e vongole", 12.00), new Piatto(5, "Cacio e pepe", 12.00),
    new Piatto(6, "Tonno", 8.50), new Piatto(7, "Lasagna", 16.00)
]

export default piatti