// var i=0
// while(i<10){
//     console.log(i);
//     i++
// }

// while(i>0){
//     console.log(i)
//     i--
// }

// 1 is odd, 2 is even

// var num=50
// var i=0
// while(i<=num){
//     if(i%2==0){
//         //console.log(i+" is even");
//         console.log(`number ${i} is even`);
//         i++
//     }
//     else{
//         //console.log(i+" is odd");
//         console.log(`number ${i} is odd`);
//         i++
//     }
// }




// for(let i=0;i<=10;i++){
//     console.log(i);
// }

//prime num or not
var num1=15
flag=0

for(let i=2;i<num1;i++)
    if (num1%i==0){
        flag=flag+1
        break
        
    }
    else{
        flag=0
    }
if (flag==0){
    console.log("prime num");
}
else{
    console.log(" not prime");
}