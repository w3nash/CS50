document.addEventListener("DOMContentLoaded", (event) => {
    const updateNav = mode => {
        if (mode) {
            let nav = document.querySelectorAll(".navbar-dark, .bg-dark");
            for(let i = 0; i < nav.length; i++) {
                nav[i].classList.remove("navbar-dark");
                nav[i].classList.remove("bg-dark");
                nav[i].classList.add("navbar-light");
                nav[i].classList.add("bg-light");
            }
        } else {
            let nav = document.querySelectorAll(".navbar-light, .bg-light");
            for (let i = 0; i < nav.length; i++) {
                nav[i].classList.remove("navbar-light");
                nav[i].classList.remove("bg-light");
                nav[i].classList.add("navbar-dark");
                nav[i].classList.add("bg-dark");
            }
        }
    }

    const updateBody = mode => {
        let body = document.querySelector("body");
        if (mode) {
            body.style.backgroundColor = "rgb(246, 248, 250)";
            body.style.color = "rgb(36, 41, 46)";
        } else {
            body.style.backgroundColor = "rgb(13, 17, 23)";
            body.style.color = "rgb(201, 209, 217)";
        }
    }

    const updateFooter = mode => {
        let items = document.querySelectorAll("a.btn-floating");
        if (mode) {
            for (let i = 0; i < items.length; i++) {
                items[i].style.color = "rgb(36, 41, 46)";
            }
        } else {
            for (let i = 0; i < items.length; i++) {
                items[i].style.color = "rgb(201, 209, 217)";
            }
        }
        
    }

    let preferColor = document.querySelector("#prefer-color");
    preferColor.addEventListener("click", (event) => {
        let icon = document.querySelector("#prefer-color-button");
        if (icon.classList.contains("fa-sun")) {
            updateNav(icon.classList.contains("fa-sun"));
            updateBody(icon.classList.contains("fa-sun"));
            updateFooter(icon.classList.contains("fa-sun"));
            icon.classList.remove("fa-sun");
            icon.classList.add("fa-moon");
        } else {
            updateNav(icon.classList.contains("fa-sun"));
            updateBody(icon.classList.contains("fa-sun"));
            updateFooter(icon.classList.contains("fa-sun"));
            icon.classList.remove("fa-moon");
            icon.classList.add("fa-sun");
        }
    });
});