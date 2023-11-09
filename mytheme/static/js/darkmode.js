// set theme based on useDarkMode
function updateBSTheme() {
    if(localStorage.getItem("useDarkMode") == "1") {
        document.documentElement.setAttribute('data-bs-theme','dark')
    }
    else {
        document.documentElement.setAttribute('data-bs-theme','light')
    }
}


if(localStorage.getItem("useDarkMode") == null) {
    localStorage.setItem("useDarkMode","0")
}

updateBSTheme()

document.addEventListener("DOMContentLoaded", function() {
    setupToggle();
});


function setupToggle() {
    if(localStorage.getItem("useDarkMode") == "1") {
        document.getElementById('darkMode').checked = true;
    }
    
    document.getElementById('darkMode').addEventListener('click',()=>{
        if(localStorage.getItem("useDarkMode") == "1") {
            localStorage.setItem("useDarkMode","0")
        }
        else {
            localStorage.setItem("useDarkMode","1")
        }
    
        updateBSTheme();
    })
}
