const pages = ["Configuration", "manageSearch", "dashboard", "activity", "documentation", "newSearch", "results"];


const firebaseConfig = {
    apiKey: "AIzaSyAwx9dACKU9zOZypdg_En2mQGcLo5E3ME4",
    authDomain: "project-genesis-21.firebaseapp.com",
    databaseURL: "https://project-genesis-21-default-rtdb.firebaseio.com",
    projectId: "project-genesis-21",
    storageBucket: "project-genesis-21.appspot.com",
    messagingSenderId: "957797207090",
    appId: "1:957797207090:web:aa8f09c4b1bc74b771c02b",
    measurementId: "G-NC95N7MJEC"
  };
  
  
  // Initialize Firebase
  firebase.initializeApp(firebaseConfig);

read()


  function read(){  


    firebase.database().ref('searchTest1/').on('value',(snap)=>{
    renderHTML(snap.val());;})
    }
  
    function renderHTML(value){
        innerHTML = "<div class = 'boxContainer1'><div class='Cboxs'>";
      for(i in value){
        innerHTML += '<a class="Cbox" href="#"><span class="Cbox-header"><iframe src = "' + value[i][
            "link"] + 'embed"></iframe></span><span class="Cbox-summary"> Account Name : ' + value[i][
                         "account"] + '<br><hr>Posted:<p>' + value[i]["postTime"] + '</p></span></a>'
      }

      innerHTML += "</div></div>"
      document.getElementById("resultRender").innerHTML = innerHTML;
  
  }


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