dispatcher-intro2libsys
=======================

Flask dispatcher for intro2libsys.info

## Adding a new Flask application 

1.  Clone the new project into the root directory, `git clone http://github.com/project-url project`

1.  Change directories into the dispatcher root directory, `cd dispatcher-intro2libsys`

1.  Create a symbolic link between the dispacher root directory and the cloned new project directory
    you created in the first step. `ln -s full-path-of-new-project new-project`

1.  For Windows, 


## Running under uwsgi 

1.  To run the dispatcher application, run the following command:
    `uwsgi -s /tmp/uwsgi.sock -w dispatcher:application --chmod-socket=666 &`


