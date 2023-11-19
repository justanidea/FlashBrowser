console.log("screening.js is loading in")

let screenshottingIsEnabled = false;

document.addEventListener('mousedown', function (event) {
    if (screenshottingIsEnabled) {
        if (event.button === 3) {

        }
    }
    else {
        //figuring out which button to use
    }
});

function enableScreenshotting() {
    screenshottingIsEnabled = true;
}

function readSettings() {

}

function toggleScreening() {
    screenshottingIsEnabled = !screenshottingIsEnabled;
}