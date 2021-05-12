//class-blue print,design ,pattern
//objt->real world entity
//reference= classinte kizhil nthekilm actions object kond chaiypikanam enekil we use reference
//class name
class Person{
    //setPerson(age,name){//intialisation
    constructor(age,name){//intialisation
        this.age=age //this.age ->instance variables
        this.name=name
    }
    printPerson(){
        console.log(this.age+","+this.name)
    }

}
//create obj in python
//referencename=classname()
//obj=Person()

//create obj in javascrippt using (var , let) declaration  and new keyword
//var obj1=new Person()

// create constructor
var obj1=new Person(25,"ajay")
//calling objt
//obj1.setPerson(25,"ajay")
obj1.printPerson()


//constructor - spcal method, automatically invoked wen objt is created
// python->__init
//java->same as class name
//javascript->constructor