# Kypsila Carbon Emission Monitor (KCEM - v1.0.0)

## Requirements
- PyQt5 (pip install PyQt5)
- OpenCv (pip install opencv-python)
- Requests (pip install requests)
- NumPy (pip install numpy)
- TomTom satelite Key (Could be get free on site https://developer.tomtom.com/)

## Process Flow
- Set the Key on the script
- Set the waiting time under Worker thread of Gui
- Start the script and GUI will appear on qualitative data

## Methodology
- Blending the circles with respect to color data of the traffic flow
- More 8-bit value corresponds to higher raidus and higher center color.
- After Blending the city elements (such as buildings and parks) are inserted with a substraction on image
- Total resultant image is saved and pushed to GUI.

## ToDo
- An archived image set with different names with respect to date.
- A data generating extra script with respectful labels.
- Using the monitor as a data source for an upcoming CNN project.