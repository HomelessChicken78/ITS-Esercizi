// Litteral notation
const me={
    nome:"Cristiano",
    cognome:"Co",
    eta:21,
    indirizzo:{
        via:"via di casa mia",
        citta:"roma"
    }
}


// json-like notation
const altro={
    "nome":"Ciao",
    "cognome":"YAY"
}

console.log(me)
console.log(me.indirizzo.via)
console.log(altro)


// new object notation
const altra=new Object();

altra.nome="Rachy"
altra.gg=123

console.log(altra)





// best way
function persona(nome='',cognome=''){
    this.nome=nome;
    this.cognome=cognome;
}
persona.prototype.calcolacodicefiscale=function(){
    return "cdsaujdiw";
}
const q=new persona("ghiro", "blu")
const f=new persona("mario", "rossi");

console.log(f);
f.telefono="4178";
f.calcolacodicefiscale=function(){
    return "cdsaujdiw";
}
console.log(f);
console.log("codice fiscale:", f.calcolacodicefiscale())
console.log("codice fiscale:", q.calcolacodicefiscale())