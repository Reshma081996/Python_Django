//read num, low,upp and find num**2 and checkn num in btwn low and upp
var num=3
var low=1
var upp=150
for(let low=1;low<=upp;low++){
    let digit=low**num
    if(digit >=low && digit <=upp){
        console.log(low+"=>"+digit);

 
    }

}