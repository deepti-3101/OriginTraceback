
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
    document.getElementById("stat").innerHTML = "Database Connection Status : Connected";
    document.getElementById("stat").style.border = "3px solid lightgreen";

}


function showOverlay(){
    renderTable();
    document.getElementById("mainOverlay").style.display = "flex";
}


function renderTable(){
    document.getElementById("origintxt").innerHTML = response["iphone14"]["origin"];
    document.getElementById("statustxt").innerHTML = response["iphone14"]["Status"];
    document.getElementById("projecttxt").innerHTML = response["iphone14"]["projectname"];
    var incode = ""
    for(i in response["iphone14"]["postdetails"]){
        var inincode = "";
        for(y in response["iphone14"]["postdetails"][i]){
            if(y == "hash"){
                var ininincode = "";
                for(k in response["iphone14"]["postdetails"][i][y]){
                    ininincode += "<div class='inTab'><div class='options-tag-nnn'>"+ k + "</div><div class='country-detail'>"+ response["iphone14"]["postdetails"][i][y][k] + "</div></div>";
                }
                inincode += "<div class='inTab'><div class='options-tag-nn'>"+ y + "</div><div class='country-detail'>"+ ininincode + "</div></div>";
            }
            else{
                inincode += "<div class='inTab'><div class='options-tag-nn'>"+ y + "</div><div class='country-detail'>"+ response["iphone14"]["postdetails"][i][y] + "</div></div>";
            }
            
        }
        incode += "<div class='inTab'><div class='options-tag-n'>"+ i + "</div><div class='country-detail'>"+ inincode + "</div></div><div class='html2pdf__page-break'></div>";
    }
    document.getElementById("postslist").innerHTML = incode;

    var ql = "";
    for(i in response["iphone14"]["pQueue"]){
        ql += "<div class='inTab'><div class='options-tag-nnn'>"+ i + "</div><div class='country-detail'>"+ response["iphone14"]["pQueue"][i][0] + "<div class='options-tag-nnn'>"+ response["iphone14"]["pQueue"][i][1] + "</div></div></div>";
    }
    document.getElementById("hashqueue").innerHTML = ql;
}

function closeOverlay(){
    document.getElementById("mainOverlay").style.display = "none";
}