const arr1=[1, 2, 3]
const arr2=[...arr1] // create a copy of the array (not a pointer)

arr2.push(4)
console.log("array1 :",arr1)
console.log("array2 :", arr2)