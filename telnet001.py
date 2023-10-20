import subprocess

def grep_and_telnet(pid):
  # Get the process name.
  process_name = subprocess.check_output(["pgrep", "-f", pid]).decode("utf-8").strip()

  # Get the port number.
  port_number = subprocess.check_output(["lsof", "-Pan", "-p", pid, "-i"]).decode("utf-8").strip()

  # Telnet into the process.
  subprocess.Popen(["telnet", "localhost", port_number])

if __name__ == "__main__":
  # Get the process ID from the command line.
  pid = input("Enter the process ID: ")

  # Grep and telnet into the process.
  grep_and_telnet(pid)
