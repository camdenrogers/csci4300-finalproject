var httpRequest;
var mysql = require('mysql');

var con = mysql.createConnection({
    host: "localhost",
    user: "finaldbuser",
    password: "Myfinalpasswordislong9.",
    database: "final"
    });

con.connect(function(err) {
    if (err) throw err;
    console.log("Connected!");
    var sqlquery = INSERT INTO events_event (id, event_title) VALUES('1', 'Test event');
    con.query(sql, function (err, result) {
	if (err) throw err;
	console.log("1 record inserted");
	    });
    });



function showContentsWhenDone() {
    if (httpRequest.readyState === XMLHttpRequest.DONE) {
	if (httpRequest.status === 200) {
	        var jsonObj = JSON.parse(httpRequest.responseText);
	        var displayDiv = document.getElementById('output');
	        displayDiv.innerHTML = httpRequest.responseText;
	        //displayDiv.innerHTML = jsonObj._embedded.events[i].name;

	        /*
		      var events = jsonObj._embedded.events;
		          var ul = document.createElement("ul");
			      var output = document.querySelector("#output");
			          for(var i=0; i<events.length; i++){
				  var event = events[i].name;
				  var listItem = document.createElement("li");
				  listItem.textContent=event;
				  ul.appendChild(listItem);
				      } //for
				          output.appendChild(ul);
					      */
	        /*    con.connect(function(err) {
		          if (err) throw err;
			      console.log("Connected!");
			          var sqlquery = INSERT INTO events_event (id, event_title) VALUES('1', 'Test event');
				      con.query(sql, function (err, result) {
				          if (err) throw err;
					      console.log("1 record inserted");
					      });
					      });
					          */
        
	    } else{
		    alert('There was a problem with the request.');
		} // if
	    
    } // if
} // showContentsWhenDone                                                                                                                                                   

function makeRequest() {
    httpRequest = new XMLHttpRequest();

    if (!httpRequest) {
        alert('Cannot create an XMLHTTP instance.');
        return false;
    } // if                                                                                                                                                                 

    httpRequest.onreadystatechange = showContentsWhenDone;
    httpRequest.open('GET', 'https://app.ticketmaster.com/discovery/v2/events.json?size=200&apikey=pNOMkcfwX5Ka9v48lfsfGzUNTCyE8zaW');
    httpRequest.send();
} // makeRequest                                                                                                                                                            

document.getElementById("ajaxButton").addEventListener('click', makeRequest);
