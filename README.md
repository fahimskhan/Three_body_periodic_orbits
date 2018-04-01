# Three_body_periodic_orbits

Hunting Three-Body Periodic Orbits
The three-body problem is the problem of taking an initial set of data that specifies the positions, masses, and velocities of three bodies for some particular point in time and then determining the motions of the three bodies, in accordance with Newton’s laws of motion and of universal gravitation which are the laws of classical mechanics. Unlike two-body problems, there is no general closed-form solution for every condition and numerical methods are needed to solve and find periodic orbits. A prominent example of the classical three-body problem is the movement of a planet with a satellite around a star and a periodic solution to such a problem is the Earth, Sun and Moon. The goal of this project is to set up the physcial conditions behind the three-body problem and define a ‘search engine’ to find new periodic orbits.

### Equations of motion
As aforementioned it is not possible to analytically solve Newton’s equations of motion for periodic three-body orbits (with one exception). However, we can use numerical algorithms to solve them. The first part of the project, therefore, requires setting up the differential equations of motions for each body in the x-y plane (we will be sticking with 2-dimensional motion for simplicity) and numerically solve them using ordinary differential equation solvers like Runge-Kutta. The differential equations of motion of three bodies in a plane described by the position vectors $r_{i} = (x_{i},y_{i})$ and masses $m_{i}$ are:

$$\ddot{x_{1}} = \frac{Gm_{2}[x_{2}(t)-x_{1}(t)]}{[(x_{1}(t)-x_{2}(t))^2+(y_{1}(t)-y_{2}(t))^2]^\frac{3}{2}} - \frac{Gm_{3}[x_{1}(t)-x_{3}(t)]}{[(x_{1}(t)-x_{3}(t))^2+(y_{1}(t)-y_{3}(t))^2]^\frac{3}{2}} ------- (1)$$

$$\ddot{y_{1}} = \frac{Gm_{2}[y_{2}(t)-y_{1}(t)]}{[(x_{1}(t)-x_{2}(t))^2+(y_{1}(t)-y_{2}(t))^2]^\frac{3}{2}} - \frac{Gm_{3}[y_{1}(t)-y_{3}(t)]}{[(x_{1}(t)-x_{3}(t))^2+(y_{1}(t)-y_{3}(t))^2]^\frac{3}{2}} ------- (2)$$

We will have two more pairs of equations for $\ddot{x_{2}}$,$\ddot{y_{2}}$ ($1 \rightarrow 2 \rightarrow 3$):

$$\ddot{x_{2}} = \frac{Gm_{3}[x_{3}(t)-x_{2}(t)]}{[(x_{2}(t)-x_{3}(t))^2+(y_{2}(t)-y_{3}(t))^2]^\frac{3}{2}} - \frac{Gm_{1}[x_{2}(t)-x_{1}(t)]}{[(x_{2}(t)-x_{1}(t))^2+(y_{2}(t)-y_{1}(t))^2]^\frac{3}{2}} ------- (3)$$

$$\ddot{y_{2}} = \frac{Gm_{3}[y_{3}(t)-y_{2}(t)]}{[(x_{2}(t)-x_{3}(t))^2+(y_{2}(t)-y_{3}(t))^2]^\frac{3}{2}} - \frac{Gm_{1}[y_{2}(t)-y_{1}(t)]}{[(x_{2}(t)-x_{1}(t))^2+(y_{2}(t)-y_{1}(t))^2]^\frac{3}{2}} ------- (4)$$

And $\ddot{x_{3}}$,$\ddot{y_{3}}$ ($1 \rightarrow 3 \rightarrow 2$):

$$\ddot{x_{3}} = \frac{Gm_{1}[x_{1}(t)-x_{3}(t)]}{[(x_{3}(t)-x_{1}(t))^2+(y_{3}(t)-y_{1}(t))^2]^\frac{3}{2}} - \frac{Gm_{2}[x_{3}(t)-x_{2}(t)]}{[(x_{3}(t)-x_{2}(t))^2+(y_{3}(t)-y_{2}(t))^2]^\frac{3}{2}} ------- (5)$$

$$\ddot{y_{3}} = \frac{Gm_{1}[y_{1}(t)-y_{3}(t)]}{[(x_{3}(t)-x_{1}(t))^2+(y_{3}(t)-y_{1}(t))^2]^\frac{3}{2}} - \frac{Gm_{2}[y_{3}(t)-y_{2}(t)]}{[(x_{3}(t)-x_{2}(t))^2+(y_{3}(t)-y_{2}(t))^2]^\frac{3}{2}} ------- (6)$$
