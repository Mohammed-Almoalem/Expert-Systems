# Expert System Implementation

This repository contains several Python scripts that implement basic expert systems using forward and backward chaining techniques. The systems leverage a knowledge base to infer conclusions based on given facts.

## Files Overview

1. `DataBase-Q1.py`: Implements an expert system with a knowledge base using certainty factors (CF) to determine possible issues based on symptoms (e.g., "lights weak" leads to "battery bad" with CF=50).

2. `DataBase-Q2.py`: Similar to `DataBase-Q1.py`, but includes user-defined certainty factors to enhance inference accuracy. It provides a more interactive approach to diagnosing problems.

3. `backward-chaining.py`: Demonstrates backward chaining, a goal-driven inference method. This script determines the type of animals based on observed behaviors (e.g., "croaks & eats flies" identifies a "frog").

4. `AC_Fuzzy_Expert_System.ipynb`: A Jupyter Notebook that utilizes a fuzzy logic approach to control air conditioning settings based on temperature and fan speed, providing a user-friendly interface for parameter adjustment.

5. `forwrd-chaining.py`: Implements forward chaining to deduce information from a set of facts and a structured knowledge base. It infers the color and RGB values of animals based on their types.

## Getting Started

To run these scripts, ensure you have Python installed along with the necessary libraries. You can execute each script directly or run the Jupyter Notebook in an interactive environment.

## Usage

Each script contains examples and can be modified to test different scenarios. The expert systems can be expanded by adding more rules and facts to the knowledge base.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
