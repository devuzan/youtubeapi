from flask import Flask
from flask_restful import Resource, Api
import pafy
from unicode_tr.extras import slugify

app = Flask(__name__)
api = Api(app)


class Index(Resource):
    def get(self, url):
        video_url = url
        video = pafy.new(video_url)
        best = video.getbest()
        new_thumb = video.thumb.replace("default", "hqdefault")
        print(new_thumb)
        return {
            'title': video.title,
            'desc': video.description,
            'count':video.viewcount,
            'duration': video.duration,
            'author': video.author,
            'url': best.url,
            'thumb': new_thumb,
            'file': slugify(url+"_"+video.title),
            'id': video.videoid
        }

api.add_resource(Index, '/<string:url>')

if __name__ == '__main__':
    app.run(debug=True)
