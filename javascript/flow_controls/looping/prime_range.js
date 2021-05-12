//prime num btween 2 ranges
var low=10
var upp=40

for(i=low;i<=upp;i++){
    let flag=0
    for(let j=2;j<i;j++){
        if(i%j==0){
            flag=1
            break
            }
        else{
            flag=0
        }
    }
  
if(flag==0){
    console.log(i);
}
}
