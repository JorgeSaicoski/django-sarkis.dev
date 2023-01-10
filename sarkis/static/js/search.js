let input = document.getElementById("searchBar");
let ul = document.getElementById("listToSearch");
let pos = ul.offsetTop

function searchBar() {
    let filter = input.value.toUpperCase();

    let tr = ul.getElementsByTagName("tr");
    for (let i = 1; i < tr.length; i++) {
        let name = tr[i].getElementsByTagName("td")[0];
        let description = tr[i].getElementsByTagName("td")[1];
        let skill = tr[i].getElementsByTagName("td")[2];
        let txtValue =  name.innerText + description.innerText + skill.innerText
        if (filter.length<1){
            tr[i].style.display = "";
            tr[i].classList.remove("select")
        }else if (txtValue.toUpperCase().indexOf(filter) > -1) {
            tr[i].style.display = "";
            tr[i].classList.add("select")
        }
        else {
            tr[i].style.display = "none";
            tr[i].classList.remove("select")
        }
    }
}

