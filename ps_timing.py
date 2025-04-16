import time
import tkinter as tk

def measure_timing():
    """
    Opens a Tkinter window with two buttons:
      - "Check-In": When clicked, starts the timing and changes the window background to blue.
      - "Check-Off": When clicked, stops the timing and closes the window.
    The function returns the elapsed time in seconds.
    """
    result = {}
    window = tk.Tk()
    window.geometry("350x150")
    window.title("Timing Task")

    # Instruction label
    instruction = tk.Label(
        window, 
        text="Press 'Check-In' to begin timing.\nThen press 'Check-Off' to stop timing.",
        font=("Helvetica", 12),
        justify="center"
    )
    instruction.pack(pady=10)

    # Check-In and Check-Off button callbacks.
    def check_in():
        # Record the start time and change the background to blue.
        result["start"] = time.time()
        window.config(bg="blue")
        btn_check_in.config(state="disabled")
        btn_check_off.config(state="normal")

    def check_off():
        # Record the end time and close the window.
        result["end"] = time.time()
        window.destroy()

    # Create buttons.
    btn_check_in = tk.Button(window, text="Check-In", command=check_in, font=("Helvetica", 12))
    btn_check_in.pack(pady=5)

    btn_check_off = tk.Button(window, text="Check-Off", command=check_off, font=("Helvetica", 12))
    btn_check_off.pack(pady=5)
    # Disable the Check-Off button until Check-In is clicked.
    btn_check_off.config(state="disabled")

    # Start the Tkinter main event loop (this call is blocking until the window is destroyed).
    window.mainloop()

    if "start" in result and "end" in result:
        return result["end"] - result["start"]
    else:
        return 0.0

def main():
    # Get user inputs for the shaping procedure.
    m = int(input("Enter the observation window (number of initial attempts, m): "))
    w = float(input("Enter the probability of reinforcement (w, between 0 and 1): "))
    target = float(input("Enter target duration in seconds (between 1 and 30): "))

    # Compute the kth index using the formula: k = (m + 1) * (1 – w)
    k_value = (m + 1) * (1 - w)
    k_index = int(round(k_value))
    k_index = max(1, min(k_index, m))
    print(f"\nComputed k index (for baseline threshold selection): {k_index}")

    # Baseline Phase: Collect initial performance measurements.
    baseline_errors = []
    print(f"\n--- Baseline Phase: {m} Attempts ---")
    for i in range(m):
        input(f"\nPress Enter to start attempt {i + 1}...")
        duration = measure_timing()
        error = abs(duration - target)
        baseline_errors.append(error)
        seconds = int(duration)
        milliseconds = int((duration - seconds) * 1000)
        print(f"Attempt {i + 1}: Duration = {seconds}.{milliseconds:03d} sec | Error = {error:.3f} sec")

    # Determine the reinforcement threshold based on the kth error from baseline attempts.
    sorted_errors = sorted(baseline_errors)
    threshold_error = sorted_errors[k_index - 1]
    print(f"\nReinforcement threshold (baseline error at kth performance): {threshold_error:.3f} sec")
    
    # Reinforcement Phase: Provide continuous attempts and feedback.
    print("\n--- Reinforcement Phase ---")
    print("You will receive positive feedback if your error is at or below the threshold.")
    
    attempt = m
    while True:
        choice = input("\nPress Enter to try a new attempt (or type 'q' to quit): ")
        if choice.lower() == 'q':
            break
        attempt += 1
        duration = measure_timing()
        error = abs(duration - target)
        seconds = int(duration)
        milliseconds = int((duration - seconds) * 1000)
        print(f"Attempt {attempt}: Duration = {seconds}.{milliseconds:03d} sec | Error = {error:.3f} sec")
        if error <= threshold_error:
            print("Well done!")
        else:
            print("Keep trying!")

if __name__ == "__main__":
    main()