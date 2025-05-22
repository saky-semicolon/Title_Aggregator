from flask import Flask, render_template, jsonify
from scraper import scrape_news
import os
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route("/")
def index():
    try:
        logger.info("Starting index route")
        articles = scrape_news()

        if not articles:
            logger.warning("No articles were returned from scraper")
            return render_template("index.html", articles=[], error="Unable to fetch news at this time. Please try again later.")

        logger.info(f"Successfully fetched {len(articles)} articles")
        return render_template("index.html", articles=articles)
    except Exception as e:
        logger.error(f"Error in index route: {str(e)}")
        return render_template("index.html", articles=[], error="An error occurred while fetching news. Please try again later.")

@app.route("/api/news")
def api_news():
    try:
        logger.info("Starting api_news route")
        articles = scrape_news()

        if not articles:
            logger.warning("No articles were returned from API")
            return jsonify({"error": "No articles found"}), 404

        logger.info(f"API returning {len(articles)} articles")
        return jsonify(articles)
    except Exception as e:
        logger.error(f"Error in api_news route: {str(e)}")
        return jsonify({"error": "An error occurred while fetching news. Please try again later."}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)