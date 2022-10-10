var dns = require('dns');
var fs = require("fs");
 
function resolveme(domainname) {
 try {
  dns.resolve4(domainname, function (err, addresses) {
   if(!err) {
    console.log(domainname + " -> " + addresses[0]);
   }
  });
 } catch(err) {
	 
 }
}

if(process.argv.length < 4) {
 console.log("domain file");
 process.exit(0); 
}
dnnames = fs.readFileSync(process.argv[3]).toString();
dnnames = dnnames.split("\n");
dnnames.forEach(function (namecurr) {
 if(namecurr != "") {
  namecurr = namecurr+"."+process.argv[2];	
  resolveme(namecurr);
 }
});

