//keys
//
employee={id:1000,name:'ajay',desig:'developer',salary:25000}
console.log(employee['name']);
console.log(employee.id)

//checking for gender in dict
console.log("gender" in employee);

//create gender
employee['gender']='Male'
console.log(employee)

// for(let key of employee){
//     console.log(key);
// } //not iterable