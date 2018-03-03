import bottle
import os
import random


@bottle.route('/')
def static():
    return " "


@bottle.route('/static/<path:path>')
def static(path):
        return bottle.static_file(path, root='static/')

@bottle.post('/start')
def start():
        data = bottle.request.json
        game_id = data.get('game_id')
        board_width = data.get('width')
        board_height = data.get('height')

        head_url = '%s://%s/static/head.png' % (
            bottle.request.urlparts.scheme,
            bottle.request.urlparts.netloc
        )

        return {

        "color": "#FF0000",
         "secondary_color": "#00FF00",
         "head_url": "https://media.licdn.com/mpr/mpr/shrinknp_200_200/AAEAAQAAAAAAAAdMAAAAJDBlMDJjMjI2LTgyMWItNDc5My1iM2Q4LWQ1NDg2MWQ5YTIwNg.jpg",
         "taunt": "I hope I remember how to turn",
         "head_type": "safe",
         "tail_type": "skinny"

        }

@bottle.post('/move')
def move():
    data = bottle.request.json
    directions = ['up', 'down', 'left', 'right']
    direction = random.choice(directions)
    print directions
    return {
        'move': direction,
        'taunt': 'I hope I remember how to turn'
    }

application = bottle.default_app()

if __name__ == '__main__':
    bottle.run(
        application,
        host=os.getenc('IP', '0.0.0.0'),
        port=os.getenv('PORT', '8080'),
        debug = True
    )
