import dash

from data_processing import  load_data, process_data

from functions import date_ago, convert_date, get_gradient_color, get_current_previous_sums, create_table, hex_to_rgb\
                            , interpolate_color, gradient_color_func \
                        , calculate_mean_max_subs, calculate_mean_posts, calculate_mean_views, calculate_mean_reacts\
                        , load_stopwords_from_file

from layouts import create_layout
from callbacks import register_callbacks

import os
import sys
import logging
from dash import Dash
import dash_bootstrap_components as dbc
from flask import Flask


# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

try:
    from layouts import create_layout
    from callbacks import register_callbacks
    from data_processing import load_data, process_data
except ImportError as e:
    logger.error(f"Error importing modules: {e}")
    sys.exit(1)

# Initialize the Flask app
server = Flask(__name__)

external_stylesheets = [
    'https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css',
    'https://fonts.googleapis.com/css?family=Merriweather|Open+Sans&display=swap',
    'Desktop/notebooks/custom-styles.css'
]

# Initialize the Dash app
app = Dash(__name__, server=server, external_stylesheets=external_stylesheets)

try:
    # Load and process data
    channels, posts, reactions, subscribers, views = load_data()
    processed_data = process_data(channels, posts, reactions, subscribers, views)

    # Create the app layout
    app.layout = create_layout(processed_data)

    # Register callbacks
    register_callbacks(app, processed_data)
except Exception as e:
    logger.error(f"Error setting up the application: {e}")
    app.layout = dbc.Container([
        dbc.Alert("An error occurred while setting up the application. Please check the logs.", color="danger")
    ])

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run_server(host='0.0.0.0', port=port, debug=False)
