# -*- coding: utf-8 -*-
"""
Created on Wed May 25 05:54:59 2016

@author: archy
"""

import web
from web import form
import subprocess

render = web.template.render('templates/')

urls = (
            '/form/','myForm',
            '/', 'index'
            
        )


myform = form.Form( 
    form.Textarea('code here'),

def inner():
    proc = subprocess.Popen(
        ['dmesg'],             #call something with a lot of output so we can see it
        shell=True,
        stdout=subprocess.PIPE
    )

    for line in iter(proc.stdout.readline,''):
        time.sleep(1)                           # Don't need this just shows the text streaming
        yield line.rstrip() + '<br/>\n'


class index:
    def GET(self):       
        return render.index("world")
        
class myForm:
    def GET(self): 
        form = myform()
        # make sure you create a copy of the form by calling it (line above)
        # Otherwise changes will appear globally
        return render.formtest(form)

    def POST(self): 
        form = myform() 
        if not form.validates(): 
            return render.formtest(form)
        else:
            # form.d.boe and form['boe'].value are equivalent ways of
            # extracting the validated arguments from the form.
            return Results
        
if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
    
    
    