//element.hide();

element.append('<span id="reset"> Options: <button>Clear</button></span>');
element.append('<span id="eraser"> <button onclick="">Eraser</button></span>');
element.append('<span id="marker"> <button>Marker</button></span>');
element.append('<div id="sketch" style="position:absolute; left:0;"><canvas id="paint"></canvas></div>');

var canvas = element.get(0).querySelector("#sketch canvas"); //childNodes[0].childNodes[0];
var ctx = canvas.getContext('2d');
var sketch = element.get(0).childNodes[3];

element.get(0).querySelector("#reset button").onclick = function() {
resetCanvas()
};
element.get(0).querySelector("#eraser button").onclick = function() {
getColor('#333333');
getSize('20');
};
element.get(0).querySelector("#marker button").onclick = function() {
getColor('green');
getSize('5');
};

canvas.style.backgroundColor = '#333333';

var sketch_style = getComputedStyle(sketch);
canvas.width = $("div.container.slides").get(0).clientWidth; 

canvas.height = $("div.container.slides").get(0).clientHeight;

var mouse = {
    x: 0,
    y: 0
};

/* Mouse Capturing Work */
canvas.addEventListener('mousemove', function(e) {
    //    alert( [this.clientWidth, e.clientX, this.offsetLeft, e.clientY, this.offsetTop, this.getBoundingClientRect().top, this.getBoundingClientRect().left] )
    mouse.x = e.clientX - this.getBoundingClientRect().left;
    mouse.y = e.pageY - this.getBoundingClientRect().top;
}, false);

/* Drawing on Paint App */
ctx.lineJoin = 'round';
ctx.lineCap = 'round';
ctx.lineWidth = '5';

ctx.strokeStyle = "green";
function getColor(colour) {
    ctx.strokeStyle = colour;
}

var getSize = function getSize(size) {
    ctx.lineWidth = size;
}

function resetCanvas() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
}

//ctx.strokeStyle = 
//ctx.strokeStyle = document.settings.colour[1].value;

canvas.addEventListener('mousedown', function(e) {
    ctx.beginPath();
    ctx.moveTo(mouse.x, mouse.y);

    canvas.addEventListener('mousemove', onPaint, false);
}, false);

canvas.addEventListener('mouseup', function() {
    canvas.removeEventListener('mousemove', onPaint, false);
}, false);

var onPaint = function() {
    ctx.lineTo(mouse.x, mouse.y);
    ctx.stroke();
};