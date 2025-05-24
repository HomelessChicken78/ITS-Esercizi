// lo switch case è una struttura molto simile alla if:
// è sempre una condizione.
// La differenza è che quest'ultimo prende un'espressione e valuta
// a quali dei case quella espressione equivale.
// Se non equivale a nessuno va nel case default.

let id_cibo = 1
switch (id_cibo) {
    case 0:
    case 1:
        console.log(`L'id cibo ${id_cibo} corrisponde a "panino" o a "pizza".`)
        break
    case 2:
        console.log(`L'id cibo ${id_cibo} corrisponde a "mortadella"`)
        break
    case 3:
        console.log(`L'id cibo ${id_cibo} corrisponde a "bistecca"`)
        break
    case 4:
        console.log(`L'id cibo ${id_cibo} corrisponde a "salmone"`)
        break
    default:
        console.log("Non so a che cibo tu ti voglia riferire!")
}

id_cibo = 2
switch (id_cibo) {
    case 0:
    case 1:
        console.log(`L'id cibo ${id_cibo} corrisponde a "panino" o a "pizza".`)
        break
    case 2:
        console.log(`L'id cibo ${id_cibo} corrisponde a "mortadella"`)
        break
    case 3:
        console.log(`L'id cibo ${id_cibo} corrisponde a "bistecca"`)
        break
    case 4:
        console.log(`L'id cibo ${id_cibo} corrisponde a "salmone"`)
        break
    default:
        console.log("Non so a che cibo tu ti voglia riferire!")
}

id_cibo = 42
switch (id_cibo) {
    case 0:
    case 1:
        console.log(`L'id cibo ${id_cibo} corrisponde a "panino" o a "pizza".`)
        break
    case 2:
        console.log(`L'id cibo ${id_cibo} corrisponde a "mortadella"`)
        break
    case 3:
        console.log(`L'id cibo ${id_cibo} corrisponde a "bistecca"`)
        break
    case 4:
        console.log(`L'id cibo ${id_cibo} corrisponde a "salmone"`)
        break
    default:
        console.log("Non so a che cibo tu ti voglia riferire!")
}