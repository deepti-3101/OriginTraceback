const { app, BrowserWindow } = require('electron')
const path = require('path')
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
let mainLoadingWindow


function createLoadingWindow() {
  mainLoadingWindow = new BrowserWindow({
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

  mainLoadingWindow.loadFile('loadingoverlay.html')
  setTimeout(createWindow, 3000)
  


}


function createWindow() {
  mainLoadingWindow.hide()
  mainWindow = new BrowserWindow({
    width: 1000,
    height: 600,
    backgroundColor:'#0000ffff',
    transparent: true,
    webPreferences: {
      preload: path.join(__dirname, 'preload.js'),
      nodeIntegration: true
    },
    resizable: false,
  })

  mainWindow.loadFile('index.html')
  mainWindow.setMenuBarVisibility(false);


}


app.whenReady().then(() => {
  createLoadingWindow()
  app.on('activate', function () {
    if (BrowserWindow.getAllWindows().length === 0) {
      createLoadingWindow();
    }
  })
})

app.on('window-all-closed', function () {
  if (process.platform !== 'darwin') app.quit()
})




