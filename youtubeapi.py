from flask import Flask
from flask_restful import Resource, Api
import pafy
from unicode_tr.extras import slugify

app = Flask(__name__)
api = Api(app)


class Index(Resource):
    def get(self, v_id):
        video_url = v_id
        video = pafy.new(video_url)
        best = video.getbest()
        new_thumb = video.thumb.replace("default", "hqdefault")
        print(new_thumb)
        return {
            'videoTitle': video.title,
            'videoDescription': video.description,
            'videoCount':video.viewcount,
            'videoDuration': video.duration,
            'channelTitle': video.author,
            'videoUrl': best.url,
            'videoThumb': new_thumb,
            'videoFileName': slugify(v_id+"_"+video.title+".mp4"),
            'videoId': video.videoid
        }

api.add_resource(Index, '/<string:v_id>')

if __name__ == '__main__':
    app.run(debug=True)
