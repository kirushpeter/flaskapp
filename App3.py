from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():

    return "<h1>go to /puppy_name/name and see the result!!</h1>"




@app.route('/puppy_name/<name>')

def puppylatin(name):

    pupname = ''

    if name[-1] == 'y':

        pupname = name[:-1] + 'iful'
    else:
        pupname = name + 'y'

        return "<h1> your puppy latin name is: {}".format(pupname)


if __name__=='__main__':
    app.run(debug = True)
