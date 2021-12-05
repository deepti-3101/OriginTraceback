const pages = ["manageSearch", "dashboard", "documentation"];


const firebaseConfig = {
    apiKey: "AIzaSyAwx9dACKU9zOZypdg_En2mQGcLo5E3ME4",
    authDomain: "project-Genesis-21.firebaseapp.com",
    databaseURL: "https://project-Genesis-21-default-rtdb.firebaseio.com",
    projectId: "project-Genesis-21",
    storageBucket: "project-Genesis-21.appspot.com",
    messagingSenderId: "957797207090",
    appId: "1:957797207090:web:aa8f09c4b1bc74b771c02b",
    measurementId: "G-NC95N7MJEC"
};


// Initialize Firebase
firebase.initializeApp(firebaseConfig);




function read(token) {
    firebase.database().ref(token + "/").on('value', (snap) => {
        console.log("got read");
        connected(snap.val());;
    })
}

function connected(value) {
    console.log("window");
    window.alert(value["agent"]);

}

console.log("here");

function connect() {
    console.log("before read");
    read(document.getElementById("tokentext").value);
    console.log("after read");
}



document.getElementById("lblbtn").addEventListener("click", function () {
    if (document.getElementById("tokentext").value) {
        connect();
    }
});



function launchSoftware() {
    document.getElementById("mainPage").style.display = "block";
    document.getElementById("credOverlayContainer").style.display = "none";

}


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

