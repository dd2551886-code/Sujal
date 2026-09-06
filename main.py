from flask import Flask, render_template_string

app = Flask(__name__)

# Single HTML template that dynamically changes content based on the page
HTML_LAYOUT = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{{ title }}</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; background-color: #f4f4f9; }
        h1 { color: #333; }
        nav a { margin-right: 15px; text-decoration: none; color: #007bff; font-weight: bold; }
        .content { margin-top: 20px; padding: 20px; background: white; border-radius: 8px; }
    </style>
</head>
<body>
    <nav>
        <a href="/">Home</a>
        <a href="/about">About</a>
    </nav>
    <div class="content">
        <h1>{{ heading }}</h1>
        <p>{{ message }}</p>
    </div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(
        HTML_LAYOUT, 
        title="Home Page", 
        heading="Welcome to My Single-File Python Website!", 
        message="This whole website, including HTML and CSS, runs from one Python file."
    )

@app.route("/about")
def about():
    return render_template_string(
        HTML_LAYOUT, 
        title="About Page", 
        heading="About This Project", 
        message="Built using Flask's render_template_string method."
    )

if __name__ == "__main__":
    app.run(debug=True)
  
