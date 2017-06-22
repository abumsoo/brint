# Notes
## Confusions
I was confused about where the flask in
  from flask import Flask
was coming from. But it makes sense because the run.py function, which starts
the web server uses the python in flask/bin/python rather than the default 
python.

We use templates, so that we don't have to write HTML directly into a return
which looks super ugly.
e.g.
  return '''
  <html>
    <body>
    this kind of crap forever
    </body>
  </html>
  '''
