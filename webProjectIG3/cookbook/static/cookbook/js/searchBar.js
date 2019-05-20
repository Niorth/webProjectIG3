function autocomplete(inp, arr) {

  	var currentFocus;

  	inp.addEventListener("input", function(e) {
		var ingredientsListDiv, ingredientDiv, i, inputVal = this.value.replace('>', '&gt');

		closeAllLists();
		if (!inputVal) { return false;}
		currentFocus = -1;

		ingredientsListDiv = document.createElement("DIV");
		ingredientsListDiv.setAttribute("id", this.id + "searchBar-list");
		ingredientsListDiv.setAttribute("class", "searchBar-items");

		this.parentNode.appendChild(ingredientsListDiv);

	    for (i = 0; i < arr.length; i++) {
	      	if(arr[i].substr(0, inputVal.length).toUpperCase() == inputVal.toUpperCase()){
	      		ingredientDiv = document.createElement("DIV");

				ingredientDiv.innerHTML = arr[i];

				ingredientDiv.innerHTML += "<input type='hidden' value='" + arr[i] + "'>";

				ingredientDiv.addEventListener("click", function(e) {

	            	inp.value = this.getElementsByTagName("input")[0].value;
	              
	              	closeAllLists();
	      		});
	      		ingredientsListDiv.appendChild(ingredientDiv);
	      	}
	    }
	});

	//arrows use
	inp.addEventListener("keydown", function(e) {
	  var searchBarListItems = document.getElementById(this.id + "searchBar-list");

	  if (searchBarListItems) {
	  	searchBarListItems = searchBarListItems.getElementsByTagName("div");
	  }

	  if (e.keyCode == 40) {//down
	    currentFocus++;
	    addActive(searchBarListItems);
	  } 
	  else if (e.keyCode == 38) { //up
	    currentFocus--;
	    addActive(searchBarListItems);
	  } 
	  else if (e.keyCode == 13) {//Enter
	    e.preventDefault();
	    if (currentFocus > -1) {
	      if (searchBarListItems) searchBarListItems[currentFocus].click();
	    }
	  }
	});


	function addActive(searchBarListItems) {
	    if (!searchBarListItems) return false;

	    removeActive(searchBarListItems);//
	    if (currentFocus >= searchBarListItems.length) currentFocus = 0;
	    if (currentFocus < 0) currentFocus = (searchBarListItems.length - 1);
	    /*add class "autocomplete-active":*/
	    searchBarListItems[currentFocus].classList.add("searchBar-active");
	}

	function removeActive(searchBarItems) {
	    for (var i = 0; i < searchBarItems.length; i++) {
	      searchBarItems[i].classList.remove("searchBar-active");
   		}
  	}

  	function closeAllLists(elmnt) {
    
		var searchBarItems = document.getElementsByClassName("searchBar-items");
	    for (var i = 0; i < searchBarItems.length; i++) {
	    	if (elmnt != searchBarItems[i] && elmnt != inp) {
	    		searchBarItems[i].parentNode.removeChild(searchBarItems[i]);
	    	}
	  	}
	}

	document.addEventListener("click", function (e) {
    	closeAllLists(e.target);
	});
}

$.ajax({
        url: $("#searchBarInput").attr("data-ajax-target"),
        success: function (data) {
          if (data) {
            autocomplete(document.getElementById("searchBarInput"), data.ingredientsName);
          }
        }
});

$.ajax({
        url: $("#searchBarTagsInput").attr("data-ajax-target"),
        success: function (data) {
          if (data) {
            autocomplete(document.getElementById("searchBarTagsInput"), data.tagsName);
          }
        }
});

$.ajax({
        url: $("#searchBarRecipeInput").attr("data-ajax-target"),
        success: function (data) {
          if (data) {
            autocomplete(document.getElementById("searchBarRecipeInput"), data.recipesName);
          }
        }
});


