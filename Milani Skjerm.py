from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Inline CSS styling for a consistent and prominent button look
CSS = """
<!DOCTYPE html>
<html lang="en">
<head>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            color: #333;
            text-align: center;
            margin: 0;
            padding: 0;
        }
        h1, h2 {
            color: #444;
        }
        .button {
            font-size: 22px;
            padding: 15px 30px;
            margin: 20px;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-weight: bold;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2);
            transition: all 0.2s ease;
            display: inline-block;
            text-decoration: none;
        }
        .button:hover {
            transform: translateY(-2px);
            box-shadow: 0px 6px 8px rgba(0, 0, 0, 0.3);
        }
        .park {
            background-color: #4CAF50;
            color: white;
        }
        .retrieve {
            background-color: #008CBA;
            color: white;
        }
        .back {
            background-color: #555;
            color: white;
        }
        form {
            margin: 20px auto;
            display: inline-block;
        }
        input {
            font-size: 18px;
            padding: 10px;
            margin: 10px;
            border-radius: 5px;
            border: 1px solid #ccc;
        }
        .container {
            padding: 20px;
        }
        .instructions {
            text-align: left;
            margin: 20px auto;
            display: inline-block;
            font-size: 18px;
        }
    </style>
</head>
<body>
    <div class="container">
"""

@app.route("/")
def main_menu():
    return f"""
    {CSS}
        <h1>Welcome to Smart Parking System</h1>
        <a class="button park" href="/park">Park Your Car</a>
        <a class="button retrieve" href="/retrieve">Retrieve Your Car</a>
    </div>
</body>
</html>
    """

@app.route("/park")
def park_screen():
    receipt_id = generate_parking_receipt_id()
    return f"""
    {CSS}
        <h2>Your parking receipt ID: {receipt_id}</h2>
        <a class="button park" href="/safety-instructions">Proceed to Safety Instructions</a>
        <a class="button back" href="/">Back to Main Menu</a>
    </div>
</body>
</html>
    """

@app.route("/safety-instructions")
def safety_instructions_screen():
    return f"""
    {CSS}
        <h2>Safety Instructions</h2>
        <div class="instructions">
            <p>1. Ensure the vehicle is shut down.</p>
            <p>2. Ensure the parking brake is engaged.</p>
            <p>3. Ensure no one is inside the car.</p>
            <p>4. Ensure all doors are locked.</p>
        </div>
        <a class="button park" href="/park-wait">Confirm and Proceed</a>
    </div>
</body>
</html>
    """

@app.route("/park-wait")
def park_wait_screen():
    return f"""
    {CSS}
        <h2>Please wait while your car is being parked...</h2>
        <script>
            setTimeout(function() {{
                window.location.href = '/end-parking';
            }}, 3000);
        </script>
    </div>
</body>
</html>
    """

@app.route("/end-parking")
def end_parking_screen():
    return f"""
    {CSS}
        <h2>Your car has been successfully parked. Thank you!</h2>
        <a class="button back" href="/">Back to Main Menu</a>
    </div>
</body>
</html>
    """

@app.route("/retrieve", methods=["GET", "POST"])
def retrieve_screen():
    if request.method == "POST":
        receipt_id = request.form.get("receipt_id", "unknown")
        return f"""
        {CSS}
            <h2>Retrieving car for receipt ID: {receipt_id}...</h2>
            <script>
                setTimeout(function() {{
                    window.location.href = '/end-retrieval';
                }}, 3000);
            </script>
        </div>
    </body>
    </html>
        """
    return f"""
    {CSS}
        <h2>Retrieve Your Car</h2>
        <form method="POST">
            <label for="receipt_id">Enter your parking receipt ID:</label>
            <input type="text" id="receipt_id" name="receipt_id" required>
            <button class="button retrieve" type="submit">Retrieve</button>
        </form>
        <a class="button back" href="/">Back to Main Menu</a>
    </div>
</body>
</html>
    """

@app.route("/end-retrieval")
def end_retrieval_screen():
    return f"""
    {CSS}
        <h2>Your car is ready for pickup. Thank you!</h2>
        <a class="button back" href="/">Back to Main Menu</a>
    </div>
</body>
</html>
    """

# Function to generate a parking receipt ID
def generate_parking_receipt_id():
    return f"R{random.randint(1000, 9999)}"

if __name__ == "__main__":
    app.run(host="172.20.10.3", port=5000, debug = True)
