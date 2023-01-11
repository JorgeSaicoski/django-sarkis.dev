let buttons = document.getElementsByClassName("button-category")
console.log(buttons)

for (i = 0; i < buttons.length; i++){
    buttons[i].addEventListener("click", ()=>{
        console.log(i-1)
        console.log(buttons[i-1].innerHTML)
    })
}