import subprocess
import time

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Command executed successfully:")
        print(result.stdout.decode())
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")
        print(e.stderr.decode())

if __name__ == "__main__":
    command = "service tor restart"  # Replace 'your_command_here' with the command you want to run
    while True:
        try:
            run_command(command)
            time.sleep(30)  # Wait for 30 seconds
        except KeyboardInterrupt:
            print("Exiting...")
            break
