function is_really_integer(n){
    return (typeof(n) === "number" && ! isNaN(n))
}

console.log(is_really_integer(10));
console.log(is_really_integer(NaN));
console.log(is_really_integer("Sono una stringa"));