const STICK_MIN = 0;
const STICK_MAX = 255;
const STICK_MED = STICK_MAX / 2;

class Report {
    constructor() {
        this.a = false;
        this.b = false;
        this.x = false;
        this.y = false;
        this.lx = STICK_MED;
        this.ly = STICK_MED;
        this.rx = STICK_MED;
        this.ry = STICK_MED;
    }
}

let currentReport = new Report();

function updateReport(input) {
    switch(input) {
        case 'a':
        case 'b':
        case 'x':
        case 'y':
            currentReport[input] = true;
            break;
        case 'l':
            currentReport.lx = STICK_MIN;
            break;
        case 'r':
            currentReport.lx = STICK_MAX;
            break;
        case 'u':
            // TODO: Where is the origin on the switch sticks?
            currentReport.ly = STICK_MAX;
            break;
        case 'd':
            currentReport.ly = STICK_MIN;
            break;
        default:
            console.error("dumbass");
    }
}

let wsUrl = window.location.toString().replace('http', 'ws') + 'websocket';
let ws = new WebSocket(wsUrl);
ws.onmessage = evt => {
    console.log(evt);
}
setInterval(() => {
    ws.send(JSON.stringify(currentReport));
    currentReport = new Report();
}, 200);