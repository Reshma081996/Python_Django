var num=212
var temp=num
var rev=0
while(num>0){
    let digit=temp%10 //2 ,1
    rev=rev+digit //0+2
    temp=temp/10//21,2
    
}
console.log(rev);