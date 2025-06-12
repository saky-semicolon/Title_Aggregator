# Title Aggregator

A web-based title aggregation tool built with Python and Flask, designed for easy deployment on platforms like Heroku and Render.

## Features

- Web scraping and title aggregation via `scraper.py`
- Simple Flask app (`app.py`) with HTML templates
- Docker and Heroku deployment support
- Configured for Render deployment using `.render.yaml`

## Project Structure
├── app.py # Main Flask application
├── scraper.py # Web scraper for title aggregation
├── templates/ # HTML templates
├── requirements.txt # Python dependencies
├── Dockerfile # Docker setup
├── Procfile # Heroku deployment config
├── .render.yaml # Render deployment config
├── web_host.txt # Hosting info or URLs
