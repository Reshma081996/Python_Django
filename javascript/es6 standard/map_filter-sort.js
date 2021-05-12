var arr=[10,20,30,40]
//var squares=arr.map(no=>no**2)
//console.log(squares);
//arr.forEach(num=>console.log(num)) print one by one
// arr.map(no=>no**2).forEach(num=>console.log(num))


// //extract even num
// var arr1=[10,21,45,20,30,40,62,65,82]
// arr1.filter(no=>(no%2==0)).forEach(no=>console.log(no))

// arr1.sort((no1,no2)=>(no1-no2)).forEach(no=>console.log(no))
// console.log("sorting")
// arr1.sort((no1,no2)=>no1>no2?-1:1).forEach(num=>console.log(num))
let num=arr.reduce((num1,num2)=>num1+num2)
console.log(num);
let min=arr.reduce((num1,num2)=>num1<num2?num1:num2)
console.log(min);
