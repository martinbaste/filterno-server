chrome.browserAction.onClicked.addListener(function(tab) {
	console.log('filterno')
	chrome.tabs.executeScript(null, {file: "get_plot.js"});
})