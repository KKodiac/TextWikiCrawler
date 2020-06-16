from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def test_main(name=None):
    main_template = 'index.html'
    return render_template(main_template, name=name)

app.run()