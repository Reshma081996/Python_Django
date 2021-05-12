//single inheritance

// class Parent{
//     m1(){ //function
//         console.log("inside parent class");
//     }
// }

// class Child extends Parent{ //INHERITANCE
//     m2(){
//         console.log("inside child class");
//     }
// }

// var child=new Child()
// child.m2()
// child.m1()

//multilevel inheritance
class Parent{
    m1(){ //function
        console.log("inside parent class");
    }
}


class Child extends Parent{ //INHERITANCE
    m2(){
        console.log("inside child class");
    }
}


class SubChild extends Child{ //INHERITANCE
    m3(){
        console.log("inside subchild class");
    }
}

var child=new SubChild()
child.m2()
child.m1()
child.m3()


//doesnt support multiple  inheritance
// a subclass cannot inherit two parent classes