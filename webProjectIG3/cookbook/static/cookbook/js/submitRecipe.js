let submitBtn = document.getElementById("submitBtn");

	submitBtn.addEventListener("click", function(e) {
	let name = document.getElementById("name").value;
	let recipe_text = document.getElementById("recipe_text").value;
	let nb_people = document.getElementById("nb_people").value;
	let ingredients = getInnerHtml($('.ingredient').toArray());
	let unit = getInnerHtml($('.unit').toArray());
	let qty = getInnerHtml($('.qty').toArray());
	let tags = getInnerHtml($('.tag').toArray());
	let csrftoken = getCookie('csrftoken');

	$.ajax({
		beforeSend: function(xhr, settings) {
	        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
	            xhr.setRequestHeader("X-CSRFToken", csrftoken);
	        }
	    },
        url: $("#submitBtn").attr("data-ajax-target"),
        method:"POST",
        data : {
        	'name' : name,
        	'recipe_text' : recipe_text,
        	'nb_people' : nb_people,
        	'ingredients' : ingredients,
        	'unit' : unit,
        	'qty' : qty,
        	'tags' : tags,
        },
        success: function (data) {
          if (data.success) {
            window.location.href = data.url;
          }
          else {
            document.getElementById("message").innerHTML = data.message
          }
        }
	});
});

function getInnerHtml(arr) {
	var result = [];
	for(var i = 0; i < arr.length; i++) {
		result.push(arr[i].innerHTML);
	}
	return result;
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function csrfSafeMethod(method) {
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}