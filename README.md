#Wat ?

Click and deploy is a tool to automatically deploy your code.
(More information is coming soon)

##How ?
##Technical details
##Add your own app to this


## Install

One shot install :
```shell
git clone https://github.com/C4ptainCrunch/click-and-deploy.git
click-and-deploy
virtualenv --distribute --no-site-packages ve
source ve/bin/activate
pip install -r requirements.txt
```

Run :

```shell
source ve/bin/activate # Do only if it's a new tty
python web.py & rqworker
```

Goto [http://127.0.0.1:5000/](http://127.0.0.1:5000/) and enjoy!

# Contribute

Fork [this](http://github.com/C4ptainCrunch/click-and-deploy/) repo, make some nice modifications, and just make a pull request :)

Once the pull request is accepted, the automatic deployer will be triggered and your modifications will be live.

## Tout doux

* Support rollbacks (and stop autodeploy is we are in rollback state)
* Support auth to prevent spamming
* Show deployement output to the user
* Log actions (to know when was the last deploy, did it went well ?)
* Be version aware : don't deploy if the source version didn't change, show last deployed version, ...
* Support app "monitoring" and make a rollback if the app is down after a deploy

# License and credits

This project is under the AGPLv3 (GNU Affero General Public License)

Copyright 2013, Nikita Marchant. All rights reserved.

This program is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This project uses :

* [Python](http://www.python.org//), an awesome high-level interpreted language <3
* [Flask](http://flask.pocoo.org/), a microframework based on Werkzeug and Jinja.
* [Fabric](http://fabfile.org/), a Python library to remotely exectue commands over ssh.
* [Flat UI](http://designmodo.github.io/Flat-UI/) : as a css framework (and thus [Bootstrap](http://getbootstrap.com))
* [Flaticons](http://flaticons.net/) for the tool icon in the header.
