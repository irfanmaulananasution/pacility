$(document).ready(function(){
	refresh();
});

function refresh() {
    $.getJSON(`getTestimonyJson`, function(result){		
		document.getElementById("testimonyShow").innerHTML = "";
		let size = result.testimony.length;
		for(i=0; i<size; i++) {
			let index = size-1-i;
			let value = result.testimony[index];
            let data3 = document.createElement("div");
            data3.innerHTML = 
`
<div class="testimony-div bg-light">
	<div class="d-flex justify-content-start">
		<div class="testimony-detail">
			<p class="testimony-title">${value.fields.username}</p>
			<p class="testimony-time">by <span class="testimony-author">${value.fields.title}</span></p>
		</div>
	</div>

	<div class="testimony-content">
		${value.fields.content}
	</div>
</div>
`;
            document.getElementById("testimonyShow").appendChild(data3);		
		}
	});
}
