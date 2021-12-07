const { app, BrowserWindow } = require('electron')
const path = require('path')




function LaunchExe() {
        var child = require('child_process').execFile;
        var executablePath = "C:\\Users\\HP\\AppData\\Local\\Temp\\tmp-22552-ItlArL9Ic1DH\\Genesis-21.exe";
        var parameters = [];
        child(executablePath, parameters, function (err, data) {
            console.log(err)
            console.log(data.toString());
        });
}

/*
var spawn = require('child_process').spawn,
ls    = spawn('cmd.exe', ['/c', "python " + path.join(__dirname, "res/G-21.py" )]);

ls.stdout.on('data', function (data) {
console.log('stdout: ' + data);
});

ls.stderr.on('data', function (data) {
console.log('stderr: ' + data);
});

ls.on('exit', function (code) {
console.log('child process exited with code ' + code);
});
*/

let mainWindow
let mainPreviewWindow

function createWindow() {
  mainWindow = new BrowserWindow({
    width: 1000,
    height: 600,
    backgroundColor:'#0000ffff',
    frame: false,
    transparent: true,
    webPreferences: {
      preload: path.join(__dirname, 'preload.js'),
      nodeIntegration: true
    },
    resizable: false,
  })

  mainWindow.loadFile('index.html')


}

function createPreviewWindow() {
  mainPreviewWindow = new BrowserWindow({
    width: 400,
    height: 600,
    show: true,
    parent: mainWindow,
    webPreferences: {
      preload: path.join(__dirname, 'preloadPreview.js')
    }
  })


  mainPreviewWindow.loadURL('http://instagram.com')
}

app.whenReady().then(() => {
  createWindow()
  LaunchExe()
 
    console.log(data.toString());
});




  app.on('activate', function () {
    if (BrowserWindow.getAllWindows().length === 0) {
      createWindow();
    }
  })
})



app.on('window-all-closed', function () {
  if (process.platform !== 'darwin') app.quit()
})


