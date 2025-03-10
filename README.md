# Cubic Bézier Curve

## Overview

This program draws a **Cubic Bézier curve** based on the provided control points. The program calculates the Bézier curve using the given mathematical formulas and then displays the graphical output. 

The Bézier curve is created using the following **control points** and **curve equations**:

- **Control Points**:
  - **Q0 = (1, 0, 0)**
  - **Q1 = (5, 5, 0)**
  - **Q2 = (15, 7, 0)**
  - **Q3 = (10, 2, 0)**

## Bézier Curve Equation

The parameter **t** is used to generate the Bézier curve. The formula for each component of the Bézier curve is as follows:

- **B0(t) = (1 - t)^3**  
- **B1(t) = 3(1 - t)^2 * t**  
- **B2(t) = 3(1 - t) * t^2**  
- **B3(t) = t^3**

The Bézier curve **B(t)** is computed using a weighted sum of the control points:

- **B(t) = B0(t) * Q0 + B1(t) * Q1 + B2(t) * Q2 + B3(t) * Q3**

## Requirements

To run the program, you will need the following Python libraries:

- **NumPy**: For numerical calculations and array manipulations.
- **Matplotlib**: For plotting the Bézier curve and control points.

These dependencies are listed in the `Pipfile`, so to install them, simply run:

```bash
pipenv install
```

To run the program and visualize the Bézier curve, execute the following command:

```bash
python bezier.py
