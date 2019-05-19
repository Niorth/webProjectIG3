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

			nbIngredients = document.getElementById("nbIngredients")
			nbIngredients.value = parseInt(nbIngredients.value) + 1

			const newLine = document.createElement('option');
			newLine.innerHTML = ingredient + " " + qty + unit;
			newLine.setAttribute("id", "option"+nbIngredients.value)


			newIngredient = document.createElement('input')
			newUnit = document.createElement('input')
			newQty = document.createElement('input')

			newIngredient.setAttribute("class", "ingredient")
			newUnit.setAttribute("class", "unit")
			newQty.setAttribute("class", "qty")

			newIngredient.setAttribute("id", "ingredient"+nbIngredients.value)
			newUnit.setAttribute("id", "unit"+nbIngredients.value)
			newQty.setAttribute("id", "qty"+nbIngredients.value)

			newIngredient.setAttribute("type", "hidden")
			newUnit.setAttribute("type", "hidden")
			newQty.setAttribute("type", "hidden")

			newIngredient.value = ingredient
			newUnit.value = unit
			newQty.value = qty

			hidden = document.getElementById("ingredientsHidden")
			hidden.appendChild(newIngredient)
			hidden.appendChild(newUnit)
			hidden.appendChild(newQty)

		    ingredientsList.appendChild(newLine);
		}	
	});

	function isAlreadyAdded(ingredient) {
		ingredients = $(".ingredient").toArray()

		for(var i = 0; i < ingredients.length; i++) {
			if(ingredients[i].value == ingredient) {
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
			idToRemove = toRemove[i].id.split("option")[1]
			document.getElementById("ingredient"+idToRemove).remove()
			document.getElementById("unit"+idToRemove).remove()
			document.getElementById("qty"+idToRemove).remove()
			toRemove[i].remove();
		}
	}
}

handleIngredientsList();