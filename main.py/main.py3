from pyngrok import ngrok
import threading
import time

# Kill previous tunnels if any
ngrok.kill()

def run_streamlit():
    !streamlit run app.py --server.port 8501

thread = threading.Thread(target=run_streamlit)
thread.start()

time.sleep(5)  # Allow server to start

public_url = ngrok.connect(8501)
print(f"Your Streamlit app is live at: {public_url}")

