from channels.routing import route, route_class
from channels.staticfiles import StaticFilesConsumer
from .consumers import ws_add, ws_disconnect, ws_message

from .ws_handlers.game_handler import ws_connect_for_game
# routes defined for channel calls
# this is similar to the Django urls, but specifically for Channels


channel_routing = [
    route("websocket.connect", ws_add),
    route("websocket.receive", ws_message),
    route("websocket.disconnect", ws_disconnect),
]
