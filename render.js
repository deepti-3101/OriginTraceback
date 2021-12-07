const pages = ["Configuration", "manageSearch", "dashboard", "activity", "documentation", "newSearch", "results","link", "addclient","content_m"];


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
  

  var platform = "";

  
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
        if (value[i]["account"] != null){
            innerHTML += '<div class="Cbox" href="#"><span class="Cbox-header"><iframe src = "' + value[i][
                "link"] + 'embed"></iframe></span><span class="Cbox-summary"> Account Name : ' + value[i][
                             "account"] + '<br><hr><h6>Posted: ' + value[i]["postTime"] + '</h6></span></div>'
                            }
          }

      innerHTML += "</div></div>"
      document.getElementById("resultRender").innerHTML = innerHTML;
  
  }


function writetofb(){
    console.log("Writing to firebase from GUI");
    console.log(document.getElementById("hashtaginput").value, document.getElementById("searchnameinput").value, document.getElementById("filepath").value);
    const dp = firebase.database().ref("networks/stream/active").set({
       hashtag : document.getElementById("hashtaginput").value,
       search_name : document.getElementById("searchnameinput").value,
       media : platform,
       file_path : document.getElementById("filepath").value


    });
}


function change_pg(){
    a=document.getElementById("url_content");
    m=console.log(a.value);
    if (m=='url'){
        OpenPage("link");
    }else {
        Openpage("content_m")
    }
}

function OpenPage(id){
    
    for(let x in pages){
        document.getElementById(pages[x]).style.display = "none";
        try{
        document.getElementById(pages[x] + "Button").className = 'test';
    }catch{
    }}
    document.getElementById(id).style.display = "block";
    document.getElementById(id + "Button").className = "active1";

    
}

function launchSoftware(){
    document.getElementById("loadingOverlayContainer").style.display = "none";
    document.getElementById("mainPage").style.display = "block";
    
}

OpenPage("manageSearch");
console.log("here");
setTimeout(launchSoftware, 5000);
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

