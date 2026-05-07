# 🎲 Monte Carlo Estimation of Pi

This project uses a probabilistic approach to estimate the value of $\pi$. By generating random points within a unit square and determining the ratio of those that fall within an inscribed circle, we can approximate the value of $\pi$ through statistical sampling.

## 📐 The Mathematics

Given a circle with radius $r$ inscribed in a square with side $2r$:

* **Area of the square**: $(2r)^2 = 4r^2$
* **Area of the circle**: $\pi r^2$
* **The Ratio**: $\frac{\text{Area of Circle}}{\text{Area of Square}} = \frac{\pi r^2}{4r^2} = \frac{\pi}{4}$

As we increase the number of random points ($N$), the ratio of points inside the circle to total points converges to $\frac{\pi}{4}$. Therefore:

$$\pi \approx 4 \times \frac{\text{Points Inside Circle}}{\text{Total Points}}$$



## 📊 Visualizing the Convergence

The animation below demonstrates how the estimate of $\pi$ stabilizes and becomes more accurate as the number of random samples increases.

![Monte Carlo Animation](images/animation.gif)

## 🛠️ Getting Started

### Prerequisites
- Python 3.x
- NumPy
- Matplotlib

### Installation & Usage
1. Clone the repository:
   ```zsh
   git clone [https://github.com/h0sseinnaderi/monte-carlo-pi-simulation.git](https://github.com/h0sseinnaderi/monte-carlo-pi-simulation.git)
