function handleIngredientsList(){
	const addIngredientButton = document.getElementById("addIngredientButton");
	const ingredientsList = document.getElementById("ingredientsList");

	addIngredientButton.addEventListener("click", function(e) {


		const ingredient = document.getElementById('searchBarInput').value;
		const unit = document.getElementById('unit').value;
		const qty = document.getElementById('qty').value;

		const nbIngredient = document.getElementById('nbIngredient').value;

		if(qty < 1) {
			return false
		}

		const newLine = document.createElement('option');
		newLine.setAttribute("value", nbIngredient);

		const newIngredient = document.createElement('SPAN');
		newIngredient.innerHTML = ingredient + ' ';
		newIngredient.setAttribute("id", 'ingredient' + nbIngredient)

		const newUnit = document.createElement('SPAN');
		newUnit.innerHTML = unit + ' ';
		newUnit.setAttribute("id", 'unit' + nbIngredient)

		const newQty = document.createElement('SPAN');
		newQty.innerHTML = qty;
		newQty.setAttribute("id", 'qty' + nbIngredient)

		newLine.appendChild(newIngredient);
		newLine.appendChild(newQty);
		newLine.appendChild(newUnit);
		

	    ingredientsList.appendChild(newLine);

	});
}

handleIngredientsList();