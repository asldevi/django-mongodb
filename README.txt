A simple comments app with django and mongoengine

usage: 

Install Fabric ($easy_install fabric), if don't have it installed yet 
Install MongoDB and make sure that "mongo" and "mongod" are in the $PATH
Now,

$fab install    #(in case you don't have django or mongoengine)
$fab mongo      # runs mongo server
$fab django     # runs the app django dev server
