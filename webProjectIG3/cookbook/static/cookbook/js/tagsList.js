function handleTagsList(){
	const addTagButton = document.getElementById("addTagButton");
	const removeTagButton = document.getElementById("removeTagButton");


	const TagsList = document.getElementById("TagsList");

	removeTagButton.addEventListener("click", function(e) {
		removeTag();
	});

	addTagButton.addEventListener("click", function(e) {


		const tag = document.getElementById('searchBarTagsInput').value.replace('<', '&lt').replace('>', '&gt');

		if(!isAlreadyAdded(tag)) {

			const newLine = document.createElement('option');

			newLine.innerHTML = tag;
			newLine.setAttribute("class", "tag");

		    tagsList.appendChild(newLine);
		}	
	});

	function isAlreadyAdded(tag) {
		tags = $('.tag').toArray();
		for(var i = 0; i < tags.length; i++) {
			if(tags[i].innerHTML == tag) {
				return true;
			}
		}
		return false;
	}

	function getSelectTags() {
	  var result = [];
	  var options = document.getElementById("tagsList").children;
	  var opt;
	  var iLen = options.length

	  for (var i=0; i<iLen; i++) {
	    opt = options[i];

	    if (opt.selected) {
	      result.push(opt);
	    }
	  }
	  return result;
	}

	function removeTag(){
		const toRemove = getSelectTags();
		for(var i = 0; i < toRemove.length; i++) {
			toRemove[i].remove();
		}
	}
}

handleTagsList();