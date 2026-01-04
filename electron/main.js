const { app, BrowserWindow } = require("electron");
const path = require("path");
const { spawn } = require("child_process");

let mainWindow;
let backendProcess;

function createWindow() {
  const preloadPath = path.resolve(__dirname, "preload.js");

  mainWindow = new BrowserWindow({
    width: 1200,
    height: 800,
    webPreferences: {
      preload: preloadPath,
      nodeIntegration: false,
      contextIsolation: true
    }
  });

  mainWindow.loadFile(path.join(__dirname, "index.html"));

  // Optional: open DevTools automatically in dev
  mainWindow.webContents.openDevTools();
}

function startBackend() {
  const scriptPath = path.resolve(__dirname, "..", "run.py");

  const condaPython = "C:\\Users\\HP\\miniconda3\\python.exe";
  const condaPath = "C:\\Users\\HP\\miniconda3";
  const condaScripts = "C:\\Users\\HP\\miniconda3\\Scripts";
  const condaLibraryBin = "C:\\Users\\HP\\miniconda3\\Library\\bin";

  backendProcess = spawn(
    condaPython,
    [scriptPath],
    {
      stdio: "inherit",
      env: {
        ...process.env,
        PATH: `${condaLibraryBin};${condaScripts};${condaPath};${process.env.PATH}`
      }
    }
  );

  backendProcess.on("error", (err) => {
    console.error("❌ Backend failed to start:", err);
  });

  backendProcess.on("exit", (code) => {
    console.error("❌ Backend exited with code:", code);
  });
}


app.whenReady().then(() => {
  startBackend();
  createWindow();
});

app.on("will-quit", () => {
  if (backendProcess) backendProcess.kill();
});
