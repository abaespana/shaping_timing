# Percentile Shaping Timing Task

## Overview

This Python project implements a timing task using a percentile shaping procedure. The program:
- Prompts the user to input an observation window (*m*), the probability of reinforcement (*w*), and a target duration (between 1 and 30 seconds).
- In the **baseline phase**, the user completes *m* attempts where they indicate their estimated duration using a simple GUI. Instead of showing an ongoing timer, a visual cue (changing the window background to blue) signals that the timing is being measured.
- The program calculates the absolute error for each attempt (i.e. the difference between the target duration and the attempt) and uses the formula

  \[
  k = (m+1) \times (1-w)
  \]

  to determine the reinforcement threshold based on the kth-best performance.
- In the **reinforcement phase**, for each subsequent attempt the program compares the error with the threshold. If the error is within the threshold, the user receives positive feedback ("Well done!"); otherwise, they are encouraged to keep trying.

## System Requirements

- **Python:** Version 3.6 or higher.
- **Tkinter:** Included in most standard Python installations on macOS and Windows. (Linux users may need to install Tkinter separately, e.g., using `sudo apt-get install python3-tk` on Debian/Ubuntu.)
  
The program is optimized for both macOS and Windows. Linux is supported provided Tkinter is installed.

## Installation and Setup

### 1. Install Python
Download and install Python from [python.org](https://www.python.org/downloads/). Make sure that the Python executable is added to your system’s PATH.

### 2. Verify Tkinter Installation
Tkinter is generally installed with Python. To verify, run:
```bash
python -m tkinter
