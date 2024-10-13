from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def calculator():
    return """
    <html>
    <head>
        <title>Calculator By Manish</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                padding: 50px;
                transition: background-color 0.3s, color 0.3s;
            }
            #calculator {
                background-color: #ffffff;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0px 0px 10px 0px #00000050;
                display: inline-block;
                transition: background-color 0.3s, color 0.3s;
            }
            h1 {
                color: #333;
                transition: color 0.3s;
            }
            label {
                display: block;
                margin: 10px 0 5px;
                color: #333;
            }
            input, select {
                padding: 10px;
                margin: 10px 0;
                width: 200px;
                border: 1px solid #ccc;
                border-radius: 5px;
            }
            input[type="submit"] {
                background-color: #28a745;
                color: white;
                cursor: pointer;
                width: 220px;
            }
            input[type="submit"]:hover {
                background-color: #218838;
            }
            #result {
                margin-top: 20px;
                font-size: 20px;
                color: #333;
            }
            .dark-mode {
                background-color: #333;
                color: white;
            }
            .dark-mode input, .dark-mode select {
                background-color: #555;
                color: white;
            }
            .dark-mode input[type="submit"] {
                background-color: #007bff;
            }
            .dark-mode input[type="submit"]:hover {
                background-color: #0056b3;
            }
            .dark-mode h1 {
                color: #000000; /* Title in dark mode will be black */
            }
            .theme-toggle {
                margin-top: 20px;
                padding: 10px 20px;
                background-color: #007bff;
                color: white;
                cursor: pointer;
                border: none;
                border-radius: 5px;
            }
        </style>
        <script>
            function toggleTheme() {
                var body = document.body;
                var calculator = document.getElementById("calculator");
                
                body.classList.toggle("dark-mode");
                calculator.classList.toggle("dark-mode");

                // Change button text based on theme
                var themeButton = document.getElementById("themeButton");
                if (body.classList.contains("dark-mode")) {
                    themeButton.textContent = "Switch to Light Mode";
                } else {
                    themeButton.textContent = "Switch to Dark Mode";
                }
            }
        </script>
    </head>
    <body>
        <div id="calculator">
            <h1>Calculator By Manish</h1>
            <form method="POST" action="/calculate">
                <label>Enter first number:</label>
                <input type="number" name="n1" required><br>

                <label>Enter second number:</label>
                <input type="number" name="n2" required><br>

                <label>Select an operator:</label>
                <select name="opr" required>
                    <option value="add">+</option>
                    <option value="sub">-</option>
                    <option value="mul">*</option>
                    <option value="div">/</option>
                </select><br>

                <input type="submit" value="Calculate">
            </form>
            <button class="theme-toggle" id="themeButton" onclick="toggleTheme()">Switch to Dark Mode</button>
        </div>
    </body>
    </html>
    """

@app.route("/calculate", methods=["POST"])
def calculate():
    try:
        n1 = float(request.form['n1'])
        n2 = float(request.form['n2'])
        oper = request.form['opr']

        if oper == "add":
            result = n1 + n2
        elif oper == "sub":
            result = n1 - n2
        elif oper == "mul":
            result = n1 * n2
        elif oper == "div":
            if n2 == 0:
                result = "Error: Division by zero is not allowed!"
            else:
                result = n1 / n2
        else:
            result = "Invalid operation."
    except ValueError:
        result = "Error: Invalid input."

    return f"""
    <html>
    <head>
        <title>Calculator By Manish - Result</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                text-align: center;
                padding: 50px;
                background-color: #f4f4f4;
            }}
            #calculator {{
                background-color: #ffffff;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0px 0px 10px 0px #00000050;
                display: inline-block;
            }}
            #result {{
                margin-top: 20px;
                font-size: 24px;
                color: #333;
            }}
            a {{
                display: inline-block;
                margin-top: 20px;
                padding: 10px 20px;
                background-color: #007bff;
                color: white;
                text-decoration: none;
                border-radius: 5px;
            }}
            a:hover {{
                background-color: #0056b3;
            }}
        </style>
    </head>
    <body>
        <div id="calculator">
            <h1>Calculator By Manish</h1>
            <div id="result">Result: {result}</div>
            <a href="/">Back to Calculator</a>
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True, port=7007)
