const services = document.getElementsByClassName("service")

function infoOpen(service){
    let p = service.getElementsByTagName("p")
    p[0].classList.remove("service-actived")
    p[0].classList.add("service-deactived")
    p[1].classList.remove("service-deactived")
    p[1].classList.add("service-actived")
}
function infoClose(service){
    let p = service.getElementsByTagName("p")
    p[0].classList.remove("service-deactived")
    p[0].classList.add("service-actived")
    p[1].classList.remove("service-actived")
    p[1].classList.add("service-deactived")
}

for (let i = 0; i < services.length; i++){
    let autoClose
    services[i].addEventListener("click",()=>{
        clearTimeout(autoClose)
        infoOpen(services[i])
    })
    document.getElementsByClassName("body-page-rigth")[0].addEventListener("mouseleave",()=>{
        clearTimeout(autoClose)
        autoClose = setTimeout(()=>{infoClose(services[i])},2500)
    })
}
