//#Find first recursive character - first adyam repeat chaiyuna character
pattern="ABBAABBA"
var dict={}
for(let ch of pattern){
    //console.log(ch);
    
    if (ch in dict){
        console.log("reversive character",ch);
        break;
           
    }
    else{
        dict[ch]=1
        }
    
    
}
