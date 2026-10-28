from flask import Flask, render_template


def create_app():
    app = Flask(__name__)

    @app.after_request
    def correct_repository_links(response):
        """Keep public links aligned with the published repository slug."""
        if response.content_type.startswith("text/html"):
            page = response.get_data(as_text=True).replace(
                "https://github.com/Sampreeth-AI/uk-ai-predeployment-evaluation",
                "https://github.com/Sampreeth-AI/testing-the-law-uk-ai-evaluation",
            )
            response.set_data(page)
        return response

    @app.get("/")
    def home():
        return render_template("index.html")

    @app.get("/health")
    def health():
        return {"status": "ok", "project": "uk-ai-predeployment-evaluation"}

    return app
