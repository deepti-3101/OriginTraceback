const pages = ["Configuration", "manageSearch", "dashboard", "activity", "documentation"];


function OpenPage(id){
    for(let x in pages){
        document.getElementById(pages[x]).style.display = "none";
        document.getElementById(pages[x] + "Button").className = 'test';
    }
    document.getElementById(id).style.display = "block";
    console.log(document.getElementById(id + "Button"));
    document.getElementById(id + "Button").className = "active1";
}

function launchSoftware(){
    document.getElementById("loadingOverlayContainer").style.display = "none";
    document.getElementById("mainPage").style.display = "block";
    
}

OpenPage("manageSearch");
console.log("here");
setTimeout(launchSoftware, 3000);
console.log("here1");

const remote = require('electron').remote;

const win = remote.getCurrentWindow(); 



document.onreadystatechange = (event) => {
    if (document.readyState == "complete") {
        handleWindowControls();

        document.getElementById('electron-ver').innerHTML = `${process.versions.electron}`
    }
};

window.onbeforeunload = (event) => {
    win.removeAllListeners();
}



/*
function handleWindowControls() {
    // Make minimise/maximise/restore/close buttons work when they are clicked
    document.getElementById('min-button').addEventListener("click", event => {
        win.minimize();
    });

    document.getElementById('max-button').addEventListener("click", event => {
        win.maximize();
    });

    document.getElementById('restore-button').addEventListener("click", event => {
        win.unmaximize();
    });

    document.getElementById('close-button').addEventListener("click", event => {
        win.close();
    });
    toggleMaxRestoreButtons();
    win.on('maximize', toggleMaxRestoreButtons);
    win.on('unmaximize', toggleMaxRestoreButtons);

    function toggleMaxRestoreButtons() {
        if (win.isMaximized()) {
            document.body.classList.add('maximized');
        } else {
            document.body.classList.remove('maximized');
        }
    }
}

*/