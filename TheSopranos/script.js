let classifier, video, label = "Loading...", speechRecognizer, speechSynth, handpose, predictions = [];
        
function setup() {
    let canvas = createCanvas(640, 480);
    canvas.parent('videoContainer');
    video = createCapture(VIDEO);
    video.hide();
    classifier = ml5.imageClassifier('MobileNet', video, modelLoaded);
    classifyVideo();
    speechRecognizer = new ml5.SpeechRec();
    speechRecognizer.onResult = speechToText;
    speechSynth = new p5.Speech();
    handpose = ml5.handpose(video, modelLoaded);
    handpose.on("predict", results => predictions = results);
}

function draw() {
    image(video, 0, 0, width, height);
    fill(255);
    textSize(24);
    text(label, 10, height - 10);
    drawHandPoints();
}

function classifyVideo() { classifier.classify(gotResult); }
function gotResult(error, results) { label = results ? results[0].label : ""; classifyVideo(); }
function modelLoaded() { console.log("Model Loaded"); }
function speechToText() { document.getElementById('speechOutput').innerText = speechRecognizer.resultString; }
function startSpeechRecognition() { speechRecognizer.start(); }
function textToSpeech() { speechSynth.speak(document.getElementById('textInput').value); }
function drawHandPoints() {
    predictions.forEach(pred => pred.landmarks.forEach(([x, y]) => ellipse(x, y, 10, 10)));
}

setup()
