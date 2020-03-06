from flask import Flask, render_template
import cbpy as cb

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    y = cb.gmatchlist()
    dlist = list();
    for x in y:
        if x not in dlist:
            dlist.append(x)

    return render_template('index.html', y=y, dlist=dlist)


@app.route('/about', methods=['GET', 'POST'])
def bout():
    return render_template('about1.html')


@app.route('/scores/<int:matid>', methods=['GET', 'POST'])
def scorecard(matid):
    x = cb.glivescore(matid + 1)
    if x[0] == "Upcoming":
        return render_template("error.html", msg=x[0])
    elif len(x) == 1:
        return render_template("error.html", msg=x[0])
    else:
        td = dict()
        td = x[8]
        bat = x[1]
        bow = x[3]
        batn = td[str(bat['id'])]
        bats = bat['score']
        bown = td[str(bow['id'])]
        bows = bow['score']
        batsman = x[5]
        bowler = x[6]

        return render_template('scores.html', x=x, teamdata=x[9], batn=batn, bown=bown, bats=bats, bows=bows,
                               batsman=batsman, bowler=bowler)


if __name__ == '__main__':
    app.run()
