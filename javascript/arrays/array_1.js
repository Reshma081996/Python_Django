// //array
// //enclosed in[]
// //insertiom order preserved
// //duplicates allowed
// //indexing
// //homogenous and heterogenous data

// var data=[10,"hello",true,10.5];
// console.log(data);

// var num=[10,20,30,40]
// console.log("index at 3 is  "+num[3]);

// var num=[10,20,60,70]
// for(let i=0;i<data.length;i++){
//     console.log(num[i])
// }

// var numbers=[100,200,601,704]
// for (let number of numbers){
//     console.log(number);
// }

// numbers.push(1001)//elt added to end of the list
// console.log(numbers);

// numbers.pop() //last elment poped out
// console.log(numbers);

//finding common elts bwteen 2 ararys
// var arr1=[10,20,30,40]
// var arr2=[21,22,30,31,40]

// for( let num of arr1){ //o(n)
//     for(let num1 of arr2){  //o(n)      
//         if (num==num1){
//             console.log(num);
//         }
//     }
// }
//total complexity (o(n**2)) high, not efficient

//e1=e2 =common elmts 10=21,20=21,30=21,30=22,30=30,coomon elts pos(e1)+1,40=30,40=31,40=40
//e1>e2 10>21,20>21,30>21,pos(e2)+1,30>22,pos(e2)+1,40>30,pos(e)+1,40>31,40
//e1<e2 10<21 pos(e1)+1,20<21,30

var arr1=[10,20,30,40]
var arr2=[21,22,30,31,40]

arr1.sort((no1,no2)=>no1-no2)
console.log(arr1);
var high1=arr1.length

arr2.sort((no1,no2)=>no1-no2)
console.log(arr2);
var high2=arr2.length

console.log(high1,high2);

var low1=0
var low2=0
//[10, 20, 30, 40 ]
//[ 21, 22, 30, 31, 40 ]
while(high1>low1 && high2>low2){
    if(arr1[low1]==arr2[low2]){//10!=21,20!=21,30!=21,30!=22,30==30,40!=31,40==40
        console.log(arr1[low1])
        low1+=1
        low2+-1
        
    }
    else if(arr1[low1]<arr2[low2]){//10<21,20<21,30<21,30<22,40<22,40<30,40<31
       
        low1+=1
    }
    else if(arr1[low1]>arr2[low2]){//30>21,30>22,40>30,40>31
        
        low2+=1 //22,30,31,40
    }
}