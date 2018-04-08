document.getElementById('currentURL').addEventListener('click', function(e) {
	e.preventDefault();
	chrome.tabs.executeScript(null, {file: "get_plot.js"});
})


document.getElementById('form').addEventListener('submit', function(e) {
	e.preventDefault();
	var kw = document.getElementById('text').value;
	window.open('http://127.0.0.1:5000/analyzekw?kw=' + encodeURIComponent(kw));
})