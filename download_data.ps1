$pythonExe = "C:\Project\myapp\venv\Scripts\python.exe"  # Update this if your Python executable has a different name or path
$pythonScript = "C:\Project\my-utils\src\main\data\data_download.py"  # Update this with the path to your Python script

# Define the time when you want to execute the Python script each day (in 24-hour format)
$executionTime = "17:10"  # Update this with the desired execution time

# Loop indefinitely
while ($true) {
    # Get the current date and time
    $currentTime = Get-Date -Format "HH:mm"

    # Compare the current time with the desired execution time
    if ($currentTime -eq $executionTime) {
        # Execute the Python script using the Python executable
        & $pythonExe $pythonScript
    }

    # Wait for a certain period of time before checking the time again
    Start-Sleep -Seconds 60
}