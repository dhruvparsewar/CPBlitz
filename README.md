# Project : CPBlitz
## How to Run CPBlitz

### 1. Prerequisites
Ensure you have Python 3 and `pip` installed on your system. 

### 2. Setup the Environment
First, open your terminal and navigate to the project directory:
```bash
cd /path/to/CPBlitz
Create a virtual environment to keep dependencies isolated:
source venv/bin/activate
Install the required Python libraries:
pip install flask requests
Make sure your virtual environment is active, then run the server file:
python3 server-logic.py
The terminal will prompt you to enter the match details:

Contestant 1 handle

Contestant 2 handle

Number of problems

Problem rating

Once you enter the rating, the script will fetch the problems from the Codeforces API. You will see a message saying Starting server... accessible to local network.

4. Connect and Play
Leave the terminal running in the background. To view the current problem link:

Host Computer: Open a web browser and navigate to http://127.0.0.1:5000

Other Players (on the same Wi-Fi/LAN): Open a web browser and enter the host's local IPv4 address followed by the port (e.g., http://192.168.1.X:5000)

The webpage will automatically refresh every 5 seconds. As soon as a problem is solved on Codeforces, the server will detect it and update everyone's page with the next problem link automatically!
