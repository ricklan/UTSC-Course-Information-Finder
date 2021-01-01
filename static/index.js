$(document).ready(function() {
	if (result !== ""){

		var formatted_result = result.replaceAll("&#34;", "\"");
		var json = JSON.parse(formatted_result);

		var result_message = "";
		for (item in json){
			if (item !== "status"){
				if (item === "Course"){
					result_message += "<span class='firstLine'>" + json[item] + "</span><br><br>";
				}
				else{
					result_message += "<b>" + item + ":</b> " + json[item] + "<br><br>";
				}
			}
		}

		if (json.status === 200){
			document.getElementById("message").innerHTML = result_message;
		}
		else if (json.status === 404){
			document.getElementById("message").innerHTML = json.message;
		}
	}
});
