console.log("preferences.js is being loaded in")

const fs = require('fs');

const store = new Preferences({
    macro: 3,
});
// let  home
// try{
//     home  = store.get('homepage');
// }
// catch (error) {
//     home  = null;
// }

class Preferences {
    constructor(opts) {
        this.path = "./preferences.json";
        this.data = parseDataFile(this.path, opts.defaults);
    }

    get(key) {
        return this.data[key];
    }

    set(key, val) {
        this.data[key] = val;
        fs.writeFileSync(this.path, JSON.stringify(this.data));
    }
}

function parseDataFile(filePath, defaults) {
    try {
        return JSON.parse(fs.readFileSync(filePath));
    } catch(error) {
        return defaults;
    }
}