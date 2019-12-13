$(document).ready(function(){
<<<<<<< HEAD
    //searchBook("web programming for babies");
    //$("#searchbook").change(function(){
    //    searchBook(document.getElementById("searchbook").value);
    //});
=======
    searchBook("web programming for babies");
    $("#searchbook").change(function(){
        searchBook(document.getElementById("searchbook").value);
    });
>>>>>>> 2a506117ce52f24bbe022021b0238bcc0d847c0d
});

function searchBook(toSearch) {
    $.getJSON(`https://www.googleapis.com/books/v1/volumes?q=${toSearch}`, function(result){
        let counter = 1;
        document.getElementsByTagName("table")[0].innerHTML = 
`
<thead>
<tr>
    <th scope="col">no.</th>
    <th scope="col">Cover</th>
    <th scope="col">Info</th>
    <th scope="col" class="text-center">Desc</th>
</tr>
</thead>
<tbody>
</tbody>
`;
        result.items.forEach(value => {
            let row = document.createElement("tr");

            let data0 = document.createElement("td");
            data0.innerText = counter;
            row.appendChild(data0);
			
			let data1 = document.createElement("td");
			var img = document.createElement("img");
			img.src = value.volumeInfo.imageLinks.thumbnail;
			img.alt = counter;
			data1.appendChild(img);
            row.appendChild(data1);

            let data2 = document.createElement("td");
            data2.innerText = "Title : " + value.volumeInfo.title + "\r\n\r\nAuthors : " + value.volumeInfo.authors.join(", ");
            row.appendChild(data2);
			
            let data3 = document.createElement("td");
            data3.classList.add("text-center");
            data3.innerHTML = 
`
<button type="button" class="btn btn-primary" data-toggle="modal" data-target="#openDesc${counter}">Open</button>
<div class="modal fade" id="openDesc${counter}" tabindex="-1" role="dialog" aria-labelledby="exampleOpenDesc${counter}" aria-hidden="true">
<div class="modal-dialog modal-lg modal-dialog-scrollable" role="document">
    <div class="modal-content">
        <div class="modal-header">
            <h5 class="modal-title" id="exampleOpenDesc${counter}"> ${value.volumeInfo.title}</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                <span aria-hidden="true">&times;</span>
            </button>
        </div>
        <div class="modal-body text-left">
            ${value.volumeInfo.description ? value.volumeInfo.description : "Empty"}
        </div>
        <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
        </div>
    </div>
</div>
</div>
`;
            row.appendChild(data3);
            document.getElementsByTagName("tbody")[0].appendChild(row);
            ++counter;
        });
    });
<<<<<<< HEAD
}

function refresh() {
	alert("masuk");
	$.getJSON('{% url \'testimony:testimony\' %}"', function(result){
		alert("2");
		var hasil = "";
		result.items.forEach(value => {
			hasil = hasil + "/r/n/" + value.volumeInfo.title;
		});
		alert(hasil);
	});
=======
>>>>>>> 2a506117ce52f24bbe022021b0238bcc0d847c0d
}