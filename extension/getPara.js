
var GlobalParas = [];

// Puts all the paragraphs into a data structure
$( document ).ready(function() {
	console.log("1")
	var ParArray = $("a[name*='par']")
	for (var i = 0; i < ParArray.length; i++) {
		var element = $(ParArray[i]).parent()[0];
		var elementType = $(element)[0].localName
		loopMax = 5
		while(elementType != "p" && loopMax != 0){
			console.log(element + " Looping cuz not para");
			element = $(element).parent()[0]
			elementType = $(element)[0].localName;
			console.log("new elementType = " + elementType)
			loopMax--;
		}
		GlobalParas.push(element);
	}
	console.log(GlobalParas.length)
	highlightParagraph(getParaByIndex(36), "rgba(255,0,0,.15)", 1)
});

function getParaByIndex(index){
	return GlobalParas[index - 1];
}

function highlightParagraph(paraElement, color, opacity){
	paraElement.innerHTML = "<mark style='background-color: " + color + "; opacity: " + opacity + ";'>" + paraElement.innerHTML + "</mark>"
}
