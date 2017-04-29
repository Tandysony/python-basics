# ''' for multi-line content 
template_html = '''
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Look at this</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link href="css/style.css" rel="stylesheet">
    </head>
    <body>
    <h1>Hello World</h1>
    <a href="https://docs.python.org/2/tutorial/inputoutput.html">python inputoutput</a>
    </body>
</html>
'''

my_html_file = open("D:/Code/Python_Learning/test_html_file.html", "w")

my_html_file.write(template_html)
my_html_file.close()
