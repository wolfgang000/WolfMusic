/**
 * @param {String} HTML representing a single element
 * @return {Element}
 */
function htmlToElement(html) {
	var template = document.createElement('template');
	template.innerHTML = html;
	return template.content.firstChild;
}

/**
 * @param {String} HTML representing any number of sibling elements
 * @return {NodeList} 
 */
function htmlToElements(html) {
	var template = document.createElement('template');
	template.innerHTML = html;
	return template.content.childNodes;
}

function makeIterator(array,startAt){
	var nextIndex = 0;
	if(startAt != null){
		nextIndex=startAt;
	}
	return {
		next: function(){
			return nextIndex < array.length ?
			{value: array[nextIndex++], index:nextIndex-1, done: false} :
			{done: true};
		}
	}
}
