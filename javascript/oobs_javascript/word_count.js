dict={}
words='hai hello hai hello hai hai'
word=words.split(" ")
console.log(word);
for(let text of word){
    if( text in dict){
        dict[text]+=1
 
    }
    else{
        dict[text]=1
        
    }
}
console.log(dict);
