
# Age of Empires 2 - Log save displayer user guide--

## Program Requirement

	-- Python3.7

## Library requirements

	-- Numpy
	-- Pandas
	-- Matplotlib
	-- PyQt5
	-- Sys (This one is usually installed default)

## GUI usage instructions

	- Initial panel provides "Open File" button as active. Click and select your file.
		- If your file is not compatible AoE2 Log Save file system will give a warning.

	- Left panel will be filled and actived on player names.
	- Overall plot will be displayed immediately after load.
	- At this point players can be activated/disactivated on overall plot through left panel.
	- Play button will start a live plot on overall data.
	- Pressing play button (which turns to pause) again will pause the live stream.
	- After pause user may contuinue from the abondoned second.
	- 2x, 4x, 16x buttons may be activated one at a time to fasten the stream.
	- Pressing activated speed button will turn stream back to 1x.
	- During live plot players can be activated/deactivated to display different players.
	- Reset button is utilized to turn everything to srating point where first file is loaded on plot.

## Features

	- Live plot on PyQt with matplotlib
	- Live plot controls as stream
	- Data read and display over live plot
	- Data members displayed on gui


