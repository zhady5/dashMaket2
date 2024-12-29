import dash

from data_processing import  load_data, process_data

from functions import date_ago, convert_date, get_gradient_color, get_current_previous_sums, create_table, hex_to_rgb\
                            , interpolate_color, gradient_color_func \
                        , calculate_mean_max_subs, calculate_mean_posts, calculate_mean_views, calculate_mean_reacts\
                        , load_stopwords_from_file

from layouts import create_layout
from callbacks import register_callbacks

channels, posts, reactions, subscribers, views = load_data()
processed_data = process_data(channels, posts, reactions, subscribers, views)


import signal
import sys

class SignalHandler:
    def __init__(self, signum, handler):
        self.signum = signum
        self.handler = handler
        self.old_handler = None

    def __enter__(self):
        self.old_handler = signal.getsignal(self.signum)
        signal.signal(self.signum, self.handler)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        signal.signal(self.signum, self.old_handler)

def sigterm_handler(signum, frame):
    print("Received SIGTERM, shutting down server...")
    sys.exit(0)

signal.signal(signal.SIGTERM, sigterm_handler)

# Настройка приложения Dash
external_stylesheets = [
    'https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css',
    'https://fonts.googleapis.com/css?family=Merriweather|Open+Sans&display=swap',
    'Desktop/notebooks/custom-styles.css'
]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets )
# Макет приложения
server = app.server

app.layout = create_layout(processed_data)
register_callbacks(app, processed_data)

if __name__ == '__main__':
     app.run_server(debug=True)
