var clk = document.querySelector("#clk")



clk.addEventListener("click",()=>{
    clk.textContent="clicked";
    clk.style.color="red"
})


var dbl=document.querySelector("#dbl")

dbl.addEventListener("dblclick",()=>{
    dbl.textContent="double clicked";
    dbl.style.color="green";
})

var mou=document.querySelector("#mou")

mou.addEventListener("mouseover",()=>{
    mou.textContent="mouse over me";
    mou.style.color="blue";
})


mou.addEventListener("mouseout",()=>{
    mou.textContent="mouse over out";
    mou.style.color="yellow";
})
