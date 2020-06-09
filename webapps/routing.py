from channels.routing import route, route_class
from channels.staticfiles import StaticFilesConsumer

from src.monopoly.ws_handlers.game_handler import ws_connect_for_game
# routes defined for channel calls
# this is similar to the Django urls, but specifically for Channels
channel_routing = [
    route("http.request","ws_connect_for_game"),
]