#!/bin/bash
# RUn all the neccessary gunicorn instances
/usr/bin/tmux new-session -s ODD_EVEN -d 'export HBNB_MYSQL_USER=root HBNB_MYSQL_PWD=root HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db; /home/ubuntu/.local/bin/gunicorn --bind 0.0.0.0:5001 web_flask.6-number_odd_or_even:app'
/usr/bin/tmux new-session -s API -d 'export HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db; /home/ubuntu/.local/bin/gunicorn --bind 0.0.0.0:5002 api.v1.app:app'
/usr/bin/tmux new-session -s HOME -d 'export HBNB_MYSQL_USER=root HBNB_MYSQL_PWD=root HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db; /home/ubuntu/.local/bin/gunicorn --bind 0.0.0.0:5003 web_dynamic.101-hbnb:app'
