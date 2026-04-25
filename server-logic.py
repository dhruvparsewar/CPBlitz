from flask import Flask

import main

app = Flask(__name__)

# explicitly setting read-only
@app.route('/', methods=['GET']) 
def home():
   
    link = main.CURRENT_LINK #import the global variable we created in main, also main is a stupid name for that file
    
    html_content = f"""
    <html>
        <head>
            <title>Codeforces Match</title>
            <meta http-equiv="refresh" content="5">
        </head>
        <body style="font-family: Arial, sans-serif; text-align: center; margin-top: 50px;">
            <h2>Current Codeforces Problem:</h2>
            <a href="{link}" target="_blank" style="font-size: 24px; color: blue;">{link}</a>
        </body>
    </html>
    """
    return html_content

if __name__ == '__main__':
    


    main.start_background_task()

    print("Starting server... accessible to local network.")
    app.run(host='0.0.0.0', port=5000)