function handleIngredientsList(){
	const addIngredientButton = document.getElementById("addIngredientButton");
	const removeIngredientButton = document.getElementById("removeIngredientButton");


	const ingredientsList = document.getElementById("ingredientsList");

	removeIngredientButton.addEventListener("click", function(e) {
		removeIngredient();
	});

	addIngredientButton.addEventListener("click", function(e) {


		const ingredient = document.getElementById('searchBarInput').value;
		const unit = document.getElementById('unit').value;
		const qty = document.getElementById('qty').value;

		if(!isAlreadyAdded(ingredient)) {

			if(qty < 1) {
				return false
			}

			const newLine = document.createElement('option');

			newLine.innerHTML = ingredient + ", " + qty + ", " + unit;

		    ingredientsList.appendChild(newLine);
		}	
	});

	function isAlreadyAdded(ingredient) {
		ingredients = []

		let ingredientOption = document.getElementById("ingredientsList").options

	    for(var i = 0; i < ingredientOption.length; i++) {
	        arr = ingredientOption[i].value.split(", ")
	        ingredients.push(arr[0])
	    }

		for(var i = 0; i < ingredients.length; i++) {
			if(ingredients[i] == ingredient) {
				return true;
			}
		}
		return false;
	}

	function getSelectIngredients() {
	  var result = [];
	  var options = document.getElementById("ingredientsList").children;
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

	function removeIngredient(){
		const toRemove = getSelectIngredients();
		for(var i = 0; i < toRemove.length; i++) {
			toRemove[i].remove();
		}
	}
}

handleIngredientsList();