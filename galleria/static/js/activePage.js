let home = document.getElementById('home');
function explorerActive(){
    home.classList.remove('active');
    document.getElementById("explorer").className = "active";
}

function uploadActive(){
    home.classList.remove('active');
    document.getElementById("upload").className = "active";
}

function profileActive(){
    home.classList.remove('active');
    document.getElementById("profile").className = "active";
}
