

function disbox(num) {
    var res=document.querySelector("#result")
    res.value+=num
    
}

function print() {
    var res=document.querySelector("#result").value
    var out=eval(res)
    document.querySelector("#result").value=out
    
}

function clearall() {
document.querySelector("#result").value="   "
    
}

function del() {
    var rest=document.querySelector("#result").value 
    var data=rest.slice(0,-1)
    document.querySelector("#result").value=data
   
    }