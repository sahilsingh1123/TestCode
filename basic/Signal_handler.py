import signal
import time

# Example 1: Handling SIGINT (Ctrl+C)
def handle_sigint(signum, frame):
    print("Received SIGINT (Ctrl+C):", signum)
    print("Cleaning up... Exiting gracefully.")
    exit(0)

# Register the handler for SIGINT
signal.signal(signal.SIGINT, handle_sigint)

# Example 2: Handling SIGTERM (Termination signal)
def handle_sigterm(signum, frame):
    print("Received SIGTERM (Termination signal):", signum)
    print("Performing shutdown tasks... Exiting.")
    exit(0)

# Register the handler for SIGTERM
signal.signal(signal.SIGTERM, handle_sigterm)

# Example 3: Handling SIGALRM (Alarm signal)
def handle_sigalrm(signum, frame):
    print("Timeout! Signal received:", signum)

# Register the handler for SIGALRM
signal.signal(signal.SIGALRM, handle_sigalrm)

# Schedule an alarm to trigger after 5 seconds
signal.alarm(5)

# Simulate a long-running process
print("Running... Press Ctrl+C to interrupt, or wait for the alarm (5 seconds).")
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("KeyboardInterrupt caught manually. Exiting.")
