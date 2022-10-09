# fastapi_simple_jinja
inspired by https://www.youtube.com/watch?v=IxXtDOI9RUo

# URL for this repo
https://github.com/pleabargain/fastapi_simple_jinja

# URLs in the app
* http://127.0.0.1:8000/docs#/default/post_basic_form_basic_post
* http://127.0.0.1:8000/docs

* http://127.0.0.1:8000/basic


# requires

* fastapi == 0.85.0
* uvicorn == 0.18.3
* python-multipart == 0.0.5

# TODO
* Create a template for a 
    * simple table
        * new page when too many rows of data returned
    * simple search
    * add data to db (session)
    * simple form

# errors
Trying to get fastapi to restart, I got an error
```
ERROR:    [Errno 10048] error while attempting to bind on address ('127.0.0.1', 8000): only one usage of each socket address (protocol/network address/port) is normally permitted

```

working  fix for me
```
(windows)
Run resmon for resource monitor dialog

On Network tab search for Listening ports section

Look for the one taking 8000 port (my case: python.exe)

taskkill.exe /PID 17280 /F
```

here's how I found that FASTAPI apparently was stil running
```netstat -aon | findstr :8000```

how to kill PID on windows.
```taskkill.exe /PID {PIDINQUESTION} /F ```

