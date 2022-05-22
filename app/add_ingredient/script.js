var add = document.getElementById('add');
add.addEventListener("click", displayDetails);


var row = 1;

function displayDetails(){
	var name= document.getElementById("name").value;
	var amount = document.getElementById("amount").value;

	if(!name || !amount){
		alert("Please fill all the boxes");
		return;
	}

	var display = document.getElementById("display");

	var newRow = display.insertRow(row);

	var cell1 = newRow.insertCell(0);
	var cell2 = newRow.insertCell(1);


	cell1.innerHTML = name;
	cell2.innerHTML = amount;

	row++;

}
