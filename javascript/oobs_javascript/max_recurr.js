pattern="ABABBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBACEEEEEEEEEEEEEE"
dict={}
let charArray=[]
let valuArray=[]
let maxCharValue=0

for(let ch of pattern){
    if (ch in dict){
        dict[ch]+=1
    }
    else{
        dict[ch]=1
    }
}


charArray=Object.keys(dict)
valuArray=Object.values(dict)
maxCharValue=Math.max(...valuArray)

console.log(charArray[valuArray.indexOf(maxCharValue)])