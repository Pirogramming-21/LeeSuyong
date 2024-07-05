let sec = document.getElementById("sec");
let msec = document.getElementById("msec");
let start = document.querySelector("#start");
let stop = document.querySelector("#stop");
let reset = document.querySelector("#reset");
let deletBtn = document.querySelector('#delete-btn')
let selectAll = document.querySelector('#selectAll')

let selfSec = 0;
let selfMsec = 0;
let timer = null
console.log(start);

start.onclick = function () {
    console.log(reset);
    console.log(selfSec);

    // selfSec = sec;
    // selfMsec = msec;
    if (timer == null) {
        timer = setInterval(updateTime, 10);
    }
}

stop.onclick = function () {
    console.log(reset);

    clearInterval(timer);
    addRecord();
}

reset.onclick = function () {
    console.log(reset);

    timer = null;
    const recordBox = document.querySelector('.footer-record')
    recordBox.innerHTML = '';
    selfSec = 0;
    selfMsec = 0;
    sec.textContent = '00';
    msec.textContent = '00';
    console.log(selfSec);
}

const updateTime = () => {

    if (selfMsec === 99) {
        selfMsec = 0;
        selfSec++;
        document.querySelector("#sec").innerHTML = selfSec;
        document.querySelector("#msec").innerHTML = selfMsec;
        console.log(selfSec)
    } else {
        selfMsec = selfMsec+1;
        // let newVar = document.querySelector("#msec").textContent
        // newVar.textContent = '${selfMsec}';
        document.querySelector("#msec").innerHTML = selfMsec;
    }
}

function addRecord() {
    const container = document.createElement('div');
    container.className = 'record-container';

    const record = document.createElement('i');
    record.className = 'fa-regular fa-circle fa-2x';
    record.addEventListener('click', () => {
            if (record.className === 'fa-regular fa-circle fa-2x') {
                record.className = 'fa-regular fa-circle-check fa-2x'
            } else if (record.className === 'fa-regular fa-circle-check fa-2x') {
                record.className = 'fa-regular fa-circle fa-2x'
            }
        }
        )
    const recordedTime = document.createElement('div');
    recordedTime.className = 'time-record';
    recordedTime.innerHTML = String(selfSec) + ' : ' + String(selfMsec) ;

    container.appendChild(record);
    container.appendChild(recordedTime);

    const recordBox = document.querySelector('.footer-record');
    recordBox.appendChild(container);
}

selectAll.onclick = function () {
    let contents = document.querySelectorAll('.record-container');
    if (selectAll.className === 'fa-regular fa-circle fa-2x') {
        selectAll.className = 'fa-regular fa-circle-check fa-2x';
        contents.forEach(content => {
            let element = content.querySelector('i');
            element.className = 'fa-regular fa-circle-check fa-2x';
        })
    } else {
        selectAll.className ='fa-regular fa-circle fa-2x';
        contents.forEach(content => {
            let element = content.querySelector('i');
            element.className = 'fa-regular fa-circle fa-2x';
        })
    }
}

deletBtn.onclick = function () {

    let contents = document.querySelectorAll('.record-container');
    contents.forEach(content => {
        document.querySelector('#selectAll').className = 'fa-regular fa-circle fa-2x';
        console.log(content)
        let identifier = content.querySelector('i');
        if (identifier.className === 'fa-regular fa-circle-check fa-2x') {
            content.remove();
        }
    })
}



