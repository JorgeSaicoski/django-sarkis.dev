const categories = document.getElementsByClassName("button-category")

const services = document.getElementsByClassName("service")

let category = "All"

for (let i = 0; i < categories.length; i++) {
	categories[i].addEventListener('click', function (){
		category = this.innerHTML
		check()
	})
}

function check() {
	for (let i = 0; i < services.length; i++) {
		let serviceCategory = services[i].getElementsByClassName("category-service")
		let list = []
		for (let a = 0; a < serviceCategory.length; a++) {
			const inner = serviceCategory[a].innerHTML
			list.push(inner)
		}
		if (category === "All" || list.includes(category)){
			services[i].classList.remove("hidden")
		}else{
			services[i].classList.add("hidden")
		}
	}
}
