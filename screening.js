console.log("screening.js is loading in")

let screenshottingIsEnabled = false;

document.addEventListener('mousedown', function (event) {
    if (screenshottingIsEnabled) {
        
        if (event.button === 3) {
            console.log("screenshottingIsEnabled, enabling python program")
            const { spawn } = require('child_process');
            const childPython = spawn('python', ['screenshot.py']);
            console.log(childPython.pid)
            childPython.stdout.on('data', (data) => {
            console.log(`${data}`)
            });
        }
    }
    else {
        //figuring out which button to use
    }
});

function enableScreenshotting() {
    console.log("never gonna give you up")
    screenshottingIsEnabled = true;
}

function disableScreenshotting() {
    screenshottingIsEnabled = false;
}

function readSettings() {

}

function toggleScreening() {
    screenshottingIsEnabled = !screenshottingIsEnabled;
}