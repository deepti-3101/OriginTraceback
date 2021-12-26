
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

firebase.initializeApp(firebaseConfig);

var response = "";

read()

function read() {


    firebase.database().ref('results/').on('value', (snap) => {
        renderHTML(snap.val());;
    })
}

function renderHTML(value) {
    console.log(value);
    response = value;
    innerHTML = "<div class = 'boxContainer1'><div class='Cboxs'>";
    for (i in value) {
        console.log(i);
        innerHTML += "<tr><td data-title='Project Name'>" + i + "</td><td data-title='Platform'>Instagram</td><td data-title='Search Status'>" + value[i]["Status"] + "</td><td data-title='Origin'>" + value[i]["origin"] + "</td><td class='select'><div class='button' onclick = 'showOverlay()'>INFO</div></td></tr>";
    }
    document.getElementById("mainList").innerHTML = innerHTML;

}


function showOverlay(){
    renderTable();
    document.getElementById("mainOverlay").style.display = "flex";
}


function renderTable(){
    document.getElementById("origintxt").innerHTML = response["iphone14"]["origin"];
    document.getElementById("statustxt").innerHTML = response["iphone14"]["Status"];
}

function closeOverlay(){
    document.getElementById("mainOverlay").style.display = "none";
}