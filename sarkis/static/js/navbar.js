const navbar = document.getElementById("navbar")
document.getElementById("close-navbar").style.display = "none";
document.getElementById("menu-navbar").style.display = "";

function changeOpen(){
    if (opened){
        navbar.classList.remove('navbar-active')
        document.getElementById("close-navbar").style.display = "none";
        document.getElementById("menu-navbar").style.display = "";

    }else{
        navbar.classList.add('navbar-active')
        document.getElementById("close-navbar").style.display = "";
        document.getElementById("menu-navbar").style.display = "none";
    }
    opened = !opened
}
let opened = false
navbar.addEventListener("click",()=>{
    changeOpen()
})