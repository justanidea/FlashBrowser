console.log("preferences.js is being loaded in")

const fs = require('fs');

const logPath = 'log.txt';


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
    updateInstantly: true,
    screensSavedPath: '.\\saved\\'
});
// let  home
// try{
//     home  = store.get('homepage');
// }
// catch (error) {
//     home  = null;
// }

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
    const instantUpdateDiv = document.getElementById('instantUpdateLabel');
    instantUpdateDiv.innerText = 'Update instantly: ' + preferences.get('updateInstantly');
    const screenshotFolderDiv = document.getElementById('screenshotFolderLabel');
    screenshotFolderDiv.innerText = preferences.get('screensSavedPath');
    updateLogs();
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
    choosingMacro = !choosingMacro;
    if (choosingMacro) {
        screenToggleFalse();
        element.setAttribute('src', "icons\\icon-macro-highlighted.png");
    }
    else {
        element.setAttribute('src', "icons\\icon-macro.png");
    }
}

function toggleUpdateInstantly() {
    preferences.set('updateInstantly', !preferences.get('updateInstantly'))
}

document.addEventListener('mousedown', function (event) {
    if (screenActive) {
        if (typeof preferences.get('macro') === 'number' && Number.isInteger(preferences.get('macro'))) {
            if (event.button === preferences.get('macro')) {
                callPython();
            }
        }
    }
    else if (choosingMacro) {
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
    if (screenActive) {
        if (typeof preferences.get('macro') === 'string') {
            if (event.button === preferences.get('macro')) {
                callPython();
            }
        }
    }
    else if (choosingMacro) {
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

function callPython() {
    console.log("screenshottingIsEnabled, enabling python program")
    const { spawn } = require('child_process');
    const childPython = spawn('python', ['screenshot.py']);
    console.log(childPython.pid)
    childPython.stdout.on('data', (data) => {
        console.log(`${data}`)
    });
    updateLogs();
}