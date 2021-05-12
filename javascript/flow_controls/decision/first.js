num=193
let res=0
let temp=num
while(temp>0){ //153>0
    let digit=temp%10 //153%10=3
    res=res+digit**3//3**3
    temp=parseInt(temp/10) //15
} 
if (res==num){
    console.log(`${num} is an armstrong number`);
    }
else{
    console.log(`${num} is not an armstrong number`);

}
