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

			const newIngredient = document.createElement('SPAN');
			newIngredient.innerHTML = ingredient;
			newIngredient.setAttribute("class", 'ingredient');

			const newUnit = document.createElement('SPAN');
			newUnit.innerHTML = unit;
			newUnit.setAttribute("class", 'unit')

			const newQty = document.createElement('SPAN');
			newQty.innerHTML = qty;
			newQty.setAttribute("class", 'qty')

			newLine.appendChild(newIngredient);
			newLine.appendChild(newQty);
			newLine.appendChild(newUnit);
			

		    ingredientsList.appendChild(newLine);
		}	
	});

	function isAlreadyAdded(ingredient) {
		ingredients = $('.ingredient').toArray();
		for(var i = 0; i < ingredients.length; i++) {
			if(ingredients[i].innerHTML == ingredient) {
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