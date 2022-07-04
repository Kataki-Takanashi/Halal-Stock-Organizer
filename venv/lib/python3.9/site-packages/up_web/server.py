from flask import Flask, request, render_template
from pymongo import MongoClient, ASCENDING
import json
import datetime
from bson.objectid import ObjectId
from bson.code import Code
from werkzeug import Response

app = Flask(__name__, static_folder='static', static_url_path='')

DB_NAME = 'up'
DB_DOMAIN = 'localhost'
DB_PORT = 27017
COLLECTION_NAME = 'statuses'

client = MongoClient(DB_DOMAIN, DB_PORT)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]


class MongoJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (datetime.datetime, datetime.date)):
            return obj.isoformat()
        elif isinstance(obj, ObjectId):
            return str(obj)
        return json.JSONEncoder.default(self, obj)


def jsonify(obj):
    """ jsonify with support for MongoDB ObjectId
    """
    return Response(json.dumps(obj, cls=MongoJsonEncoder), mimetype='application/json')


@app.route("/aggregate/by_name/")
def by_name():
    data = []

    if 'name' in request.args:
        cursor = collection.find({
            'path': request.args['name']
        })
        cursor.sort('date', ASCENDING)
        data = list(cursor)

    return jsonify(data)


@app.route("/aggregate/by_name/by_upness")
def by_name_by_upness():
    """
    From: https://gist.github.com/RedBeard0531/1886960
    """
    data = []

    upness_map = Code("""
        function map() {
            emit(this.path, // Or put a GROUP BY key here
                 {sum: this.up, // the field you want stats for
                  min: this.up,
                  max: this.up,
                  count:1,
                  diff: 0, // M2,n:  sum((val-mean)^2)
            });
        }
    """)

    upness_reduce = Code("""
        function reduce(key, values) {
            var a = values[0]; // will reduce into here
            for (var i=1/*!*/; i < values.length; i++){
                var b = values[i]; // will merge 'b' into 'a'


                // temp helpers
                var delta = a.sum/a.count - b.sum/b.count; // a.mean - b.mean
                var weight = (a.count * b.count)/(a.count + b.count);

                // do the reducing
                a.diff += b.diff + delta*delta*weight;
                a.sum += b.sum;
                a.count += b.count;
                a.min = Math.min(a.min, b.min);
                a.max = Math.max(a.max, b.max);
            }

            return a;
        }
    """)

    upness_finalize = Code("""
        function finalize(key, value){
            value.avg = value.sum / value.count;
            value.variance = value.diff / value.count;
            value.stddev = Math.sqrt(value.variance);
            return value;
        }
    """)

    reduced = collection.map_reduce(upness_map, upness_reduce, 'reduced-by-upness', finalize=upness_finalize)
    data = list(reduced.find())

    return jsonify(data)


@app.route("/annotations/")
def annotations():
    cursor = db.annotations.find()
    cursor.sort('date', ASCENDING)
    data = list(cursor)

    return jsonify(data)


@app.route('/')
def home():
    paths = collection.distinct('path')
    paths.sort()

    return render_template('home.html', paths=paths)


@app.route('/lava/')
def lava():
    return render_template('lava.html')


def main(debug=True):
    """
    Start the server for the application.
    """
    app.debug = debug
    app.run(host='0.0.0.0')

if __name__ == "__main__":
    main()
