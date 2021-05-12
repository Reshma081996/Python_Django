//Polymoriphsm
//overloading=>methods wid same name and different num of args,
              //=>recently implented method work avulluu
//overriding

class Calc{
    add(){
        console.log("inside no arg");
    }
    add(num1){
        console.log("inside 1 arg")
    }
    add(num1,num2){
        console.log("inside 2 args");
    }
}
var obj=new Calc()
obj.add(10) 
obj.add()
obj.add(10,20)
//=> last recently implented method work avulluu
