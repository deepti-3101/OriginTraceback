
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
        innerHTML += "<tr><td data-title='Project Name'>" + i + "</td><td data-title='Platform'>Instagram</td><td data-title='Search Status'>" + value[i]["Status"] + "</td><td data-title='Origin'>" + value[i]["origin"] + "</td><td class='select'><div class='button' onclick = 'showOverlay(\"" + String(i) + "\")'>INFO</div></td></tr>";
    }
    document.getElementById("mainList").innerHTML = innerHTML;
    document.getElementById("stat").innerHTML = "Database Connection Status : Connected";
    document.getElementById("stat").style.border = "3px solid lightgreen";

}


function showOverlay(tag){
    renderTable(tag);
    document.getElementById("mainOverlay").style.display = "flex";
}


function renderTable(value){
    
    document.getElementById("origintxt").innerHTML = response[value]["origin"];
    document.getElementById("statustxt").innerHTML = response[value]["Status"];
    document.getElementById("projecttxt").innerHTML = response[value]["projectname"];
    var incode = ""
    for(i in response[value]["postdetails"]){
        var inincode = "";
        for(y in response[value]["postdetails"][i]){
            if(y == "hash"){
                var ininincode = "";
                for(k in response[value]["postdetails"][i][y]){
                    ininincode += "<div class='inTab'><div class='options-tag-nnn'>"+ k + "</div><div class='country-detail'>"+ response[value]["postdetails"][i][y][k] + "</div></div>";
                }
                inincode += "<div class='inTab'><div class='options-tag-nn'>"+ y + "</div><div class='country-detail'>"+ ininincode + "</div></div>";
            }
            else{
                inincode += "<div class='inTab'><div class='options-tag-nn'>"+ y + "</div><div class='country-detail'>"+ response[value]["postdetails"][i][y] + "</div></div>";
            }
            
        }
        incode += "<div class='inTab'><div class='options-tag-n'>"+ i + "</div><div class='country-detail'>"+ inincode + "</div></div>";
    }
    document.getElementById("postslist").innerHTML = incode;

    var ql = "";
    for(i in response[value]["pQueue"]){
        ql += "<div class='inTab'><div class='options-tag-nnn'>"+ i + "</div><div class='country-detail'>"+ response[value]["pQueue"][i][0] + "<div class='options-tag-nnn'>"+ response[value]["pQueue"][i][1] + "</div></div></div>";
    }
    document.getElementById("hashqueue").innerHTML = ql;
}

function closeOverlay(){
    document.getElementById("mainOverlay").style.display = "none";
}

function generatePDF() {
    document.getElementById("postslist").style.border = "none";
    const element = document.getElementById('mainCard');
    html2pdf(element, {
        margin: 10,
        filename: 'Genesis-21(Result).pdf',
        image: { type: 'jpeg', quality: 1 },
        html2canvas: { scale: 3, logging: true, dpi: 216, letterRendering: true },
        jsPDF: { unit: 'mm', format: 'a4', orientation: 'portrait' }
    });
}