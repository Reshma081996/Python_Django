class Employee{
    constructor(eid,name,sal,desig){
        this.eid=eid
        this.name=name
        this.sal=sal
        this.desig=desig
    }
    printDetails=()=>{
        console.log(this.eid+this.name+this.sal);
    }
}
var employee=[]
var emp1=new Employee(100,"varun",25000,"developer")
var emp2=new Employee(101,"arun",22000,"developer")
var emp3=new Employee(102,"ravi",23000,"qa")
var emp4=new Employee(100,"varun",27000,"qa")
employee.push(emp1)
employee.push(emp2)
employee.push(emp3)
employee.push(emp4)

employee.forEach(emp=>console.log(emp.desig))
employee.map(emp=>emp.sal+2000).forEach(sal=>console.log(sal))
employee.map(emp=>emp.name.toUpperCase()).forEach(emp=>console.log(emp))
//mapinte case il for eachil mapil ninu kittiya value verum
employee.filter(emp=>emp.desig=="developer").forEach(emp=>console.log(emp))
//condition meet chaiytha complete obj passavind foreach

//based on salary , sort employee
employee.sort((o1,o2)=>o1.sal>o2.sal?-1:1).forEach(emp=>console.log(emp))

// if(obj1.sal>obj2.sal //no1>no2
//     return -1        //return no1
// else
//     return 1
//obj1.sal>obj2.sal?-1:1 //descending order

//react(libarray),angular(framework),express

//min salary
let max_sal=employee.map(emp=>emp.sal).reduce((sal1,sal2)=>sal1>sal2?sal1:sal2)
console.log(max_sal);


// mean stack

// m;mongodog,mysql
// e- expresssjs backnd framework(javascript)
// a-angular(front end frameork javascript)
// react-react(frontend javascript library)
// n=node(back end javascript)