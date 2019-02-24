var page = require('webpage').create();
page.open('/users/ajmcvitt/bin/putwhateverthen/map.html', function() {

	page.viewportSize = {
		  width: 1366,
		  height: 768
	};
	window.setTimeout(function() {
  page.render('/users/ajmcvitt/www/htv3/desktop.png');
  phantom.exit();

}, 3000);

});
