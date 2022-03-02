# %% [markdown]
# ### Energetic Balls
#
# Two equivalent balls are dropped simultaneously from two ramps as shown in the figure (assuming the friction force on the ramps is negligible, and note that the mechanical energies of the balls are equal throughout the process):

# %% [markdown]
# ![energetic_balls.jpg](attachment:8816e8b3-a04c-4b4c-a570-6a7d946b86ba.jpg)

# %% [markdown]
# (Let's assume that the lowest points of the ramps are at the same level - the start and end heights are also at the same height)
#
# Taking the mass of the balls 1 kg and the side of the squares 1 meter:
#
# 1. Velocity-Position
# 2. Position-Time
#
# Let's draw the graphs.
#
# (their kinetic energy at the end of the ramps, hence their speed will be equal)

# %%
import numpy as np
import matplotlib.pyplot as plt

# The values of the red path
y1 = np.array([4, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3])

# The values of the blue path
y2 = np.array([4, 3.5, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 1, 2, 3, 3, 3])

# %%
x = np.arange(0, 18)
plt.plot(x, y1, "r-")
plt.plot(x, y2, "b-")
plt.xticks(x)
plt.grid(True)
plt.show()

# %%
m = 1  # kg
g = 9.8  # m/s^2

Pot_E1 = m*g*y1  # potential energy of the ball on the red path
Pot_E2 = m*g*y2  # potential energy of the ball on the blue path

# we get initial speeds to zero
v1 = [0]
v2 = [0]

N = x.size

for i in range(1, N):
    # change in kinetic energy of the ball on the red path
    Delta_Kin_E1 = -(Pot_E1[i] - Pot_E1[i-1])
    # change in kinetic energy of the ball on the blue path
    Delta_Kin_E2 = -(Pot_E2[i] - Pot_E2[i-1])
    v1.append(np.sqrt(v1[i-1]**2 + 2*Delta_Kin_E1/m))
    v2.append(np.sqrt(v2[i-1]**2 + 2*Delta_Kin_E2/m))

plt.plot(x, v1, "ro-")
plt.plot(x, v2, "bx-")
plt.title("Velocity-Position Graph")
plt.xticks(x)
plt.grid(True)
plt.show()

print("Maximum Speed: {:.3f} m/s".format(max(v1)))
print("Final Speed: {:.3f} m/s".format(v1[-1]))

# %%
t1 = [0]
t2 = [0]

for i in range(1, N):
    t1.append(t1[-1]+2*(x[i]-x[i-1])/(v1[i]+v1[i-1]))
    t2.append(t2[-1]+2*(x[i]-x[i-1])/(v2[i]+v2[i-1]))

plt.plot(t1, x, "r.-")
plt.plot(t2, x, "b.-")
plt.grid(which="minor", alpha=0.5)
plt.grid(which="major")
plt.title("Position-Time Graph")
plt.minorticks_on()
plt.show()

# Time taken by the ball going on the red path
print("Time taken by the ball going on the red path:", t1[-1])
# Time taken by the ball going on the blue path
print("Time taken by the ball going on the blue path:", t2[-1])

# %%
