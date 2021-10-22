let features = {};
const SERVER_URL = 'http://localhost:5000'

chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
    chrome.tabs.sendMessage(tabs[0].id, {type: "getFeatures"}, function(data) {
        features = data;
    });
});

document.getElementById('checkPage').addEventListener('click', () => {
    fetch(SERVER_URL, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(features)
    }).then(res => {
        console.log(res);
    }).catch(err => {
        console.log(err);
    })
})