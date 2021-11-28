const { app, BrowserWindow } = require('electron')
const path = require('path')

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
  createPreviewWindow()
  app.on('activate', function () {
    if (BrowserWindow.getAllWindows().length === 0) {
      createWindow();
      createPreviewWindow();
    }
  })
})

app.on('window-all-closed', function () {
  if (process.platform !== 'darwin') app.quit()
})
