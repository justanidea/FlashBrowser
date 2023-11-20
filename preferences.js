console.log("preferences.js is being loaded in")

const fs = require('fs');

const logPath = 'saved\\logs.txt';


function createOrUpdateFile(path, data) {
    fs.writeFileSync(path, JSON.stringify(data));
}

class Preferences {
    constructor(opts) {
        this.path = "preferences.json";
        this.data = parseDataFile(this.path, opts);
        createOrUpdateFile(this.path, this.data);
        createOrMakeEmptyLogFile()
    }

    get(key) {
        return this.data[key];
    }

    set(key, val) {
        this.data[key] = val;
        createOrUpdateFile(this.path, this.data);
        updateSettingsDiv();
    }

}
document.addEventListener('DOMContentLoaded', function() {
    updateSettingsDiv();
});
let preferences = new Preferences({
    macro: 3,
    macroName: 'macro button name',
    uploadInstantly: true,
    screensSavedPath: '.\\saved\\screenshots\\'
});

function parseDataFile(filePath, defaults) {
    try {
        if (!fs.existsSync(filePath)) {
            return defaults;
        }
        return JSON.parse(fs.readFileSync(filePath));
    } catch(error) {
        return defaults;
    }
}

function updateSettingsDiv() {
    const keyBindDiv = document.getElementById('keyBindLabel');
    keyBindDiv.innerText = 'Key chosen: ' + preferences.get('macroName');
    const instantUpdateDiv = document.getElementById('instantUploadLabel');
    instantUpdateDiv.innerText = 'Upload instantly: ' + preferences.get('uploadInstantly');
    const screenshotFolderDiv = document.getElementById('screenshotFolderLabel');
    screenshotFolderDiv.innerText = preferences.get('screensSavedPath');
    updateLogs();
    updateAmountSaved();
    const uploadInstantlyIcon = document.getElementById('uploadIcon');
    unhoverUpdateInstantly(uploadInstantlyIcon);
}

function updateLogs() {
    const logConsoleDiv = document.getElementById('logConsole');
    if (!fs.existsSync(logPath)) {
        createOrMakeEmptyLogFile();
    }
    logConsoleDiv.innerText = fs.readFileSync(logPath);
}

function createOrMakeEmptyLogFile() {
    console.log('Creating new empty log file')
    fs.writeFileSync(logPath, '')
}

let choosingMacro = false;
function toggleChoosingMacro() {
    let element = document.getElementById('macroIcon');
    const toggleButton = document.getElementById('toggleScreeningButton')
    if (toggleButton === undefined || element === undefined) return;
    choosingMacro = !choosingMacro;
    if (choosingMacro) {
        screenToggleFalse(toggleButton);
        element.setAttribute('src', "icons\\icon-macro-highlighted.png");
    }
    else {
        element.setAttribute('src', "icons\\icon-macro.png");
    }
}

function toggleUploadInstantly() {
    preferences.set('uploadInstantly', !preferences.get('uploadInstantly'))
    const toggleButton = document.getElementById('uploadIcon')
    if (toggleButton === undefined) return;
    if (preferences.get('uploadInstantly')) {
        toggleButton.setAttribute('src', "icons\\icon-upload-turned-on.png");
    }
    else {
        toggleButton.setAttribute('src', "icons\\icon-upload-settings.png");
    }
}

document.addEventListener('mousedown', function (event) {
    if (!screenActive && choosingMacro) {
        toggleChoosingMacro();
        preferences.set('macro', event.button);
        preferences.set('macroName', getMouseButtonName(event.button));
    }
});
function getMouseButtonName(buttonCode) {
    switch (buttonCode) {
        case 0:
            return 'Left Mouse Button';
        case 1:
            return 'Middle Mouse Button';
        case 2:
            return 'Right Mouse Button';
        case 3:
            return 'First Thumb Mouse Button';
        case 4:
            return 'Second Thumb Mouse Button';
        default:
            return 'Unknown mouse Button';
    }
}
document.addEventListener('keydown', function (event) {
    if (!screenActive && choosingMacro) {
        toggleChoosingMacro();
        preferences.set('macro', event.key);
        let macroName = event.key;
        if (macroName === " " || macroName === "")
        {
            macroName = event.code;
        }
        preferences.set('macroName', macroName);
    }
});

function updateAmountSaved() {
    const element = document.getElementById('screenCount')
    if (element !== undefined) {
        element.innerText = countFiles(preferences.get('screensSavedPath'))
    }
    updateLogs()
}

function countFiles(path) {
    try {
        const files = fs.readdirSync(path);
        let fileCount = 0;

        files.forEach(file => {
            const fullPath = `${path}/${file}`;
            if (fs.statSync(fullPath).isFile()) {
                fileCount++;
            }
        });

        return fileCount;
    } catch (error) {
        console.error('Error reading directory:', error.message);
        return -1; // Return -1 to indicate an error
    }
}

// Execute the checkCondition function every 10 seconds (10000 milliseconds)
setInterval(updateAmountSaved, 10000);


function hoverUpdateInstantly(element) {
    if (preferences.get('uploadInstantly')) {
        element.setAttribute('src', "icons\\icon-upload-settings-turned-on-highlighted.png");
    }
    else {
        element.setAttribute('src', "icons\\icon-upload-settings-highlighted.png");
    }
}

function unhoverUpdateInstantly(element) {
    if (preferences.get('uploadInstantly')) {
        element.setAttribute('src', "icons\\icon-upload-turned-on.png");
    }
    else {
        element.setAttribute('src', "icons\\icon-upload-settings.png");
    }
}