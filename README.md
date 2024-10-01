# Self-Driving Car Simulation Using Fuzzy Logic

This repository hosts a simulation of a self-driving car system that utilizes fuzzy logic to control vehicle movement based on sensor inputs. The simulation assesses obstacles' proximity to the car, adjusting the steering angle appropriately to avoid collisions, and considers both the distance from obstacles and the car's speed to optimize driving decisions.

## Project Description

The simulation implements fuzzy logic principles to dynamically adjust the driving parameters of a self-driving car. Using inputs like the distance to the nearest obstacle and the car's current speed, the system calculates the optimal steering adjustments to navigate its environment safely.

### Key Features

- **Fuzzification**: Converts real sensor inputs into suitable fuzzy inputs for processing.
- **Inference**: Applies fuzzy logic rules to determine the action based on the fuzzy inputs.
- **Defuzzification**: Converts the fuzzy conclusions back into precise control commands to steer the car.

The control logic is split across two primary scripts:
- `fuzzy_controller.py`: Handles the basic fuzzy logic operations including fuzzification, inference, and defuzzification.
- `additional_controller.py`: Extends the functionality to consider additional parameters such as the car's speed and further distance metrics for refined control.

## Technologies Used

- **Python**: Primary programming language.
- **Pygame**: Used for creating the game environment.

## Setup and Running the Simulation

Clone this repository, install corresponding libraries, navigate to the directory containing the project files and run the simulation using:

```bash
python simulator.py
