module.exports = function (cb) { 
	var request = require("request");

	var AUTH0_DOMAIN = "";
    var AUTH0_CLIENT_ID = "";
    var AUTH0_CLIENT_SECRET = "";
    var AUTH0_AUDIENCE_API = "https://" + AUTH0_DOMAIN + "/api/v2/";

	var options = { method: 'POST',
	  url: 'https://' + AUTH0_DOMAIN + '/oauth/token',
	  headers: { 'content-type': 'application/json' },
	  body: 
	   { grant_type: 'client_credentials',
	     client_id: AUTH0_CLIENT_ID,
	     client_secret: AUTH0_CLIENT_SECRET,
	     audience: AUTH0_AUDIENCE_API },
	  json: true };

	request(options, function (error, response, body) {
	  if (error) throw new Error(error);

	  cb(null, body); 
	});

}
