const navbar = document.getElementById("navbar")

function changeOpen(){
    if (opened){
        navbar.classList.remove('navbar-active')
    }else{
        navbar.classList.add('navbar-active')
    }
    opened = !opened
}
let opened = false
navbar.addEventListener("click",()=>{
    changeOpen()
})