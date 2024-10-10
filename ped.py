
import matplotlib.pyplot as plt
import numpy as np

# Data points for the free energy change along the reaction coordinate
reaction_coordinate = np.array([0, 1, 2, 3, 4, 5, 6])
reaction_coordinate2 = np.array([1, 2, 3, 4, 5, 6])
delta_G_CeIII = np.array([0, -0.1, -0.3, 0.2, -0.1, -0.2, -0.3])
delta_G_CeIV = np.array([0, 0.4, -0.01, -0.1, -0.3, -0.3])

# Width for the horizontal lines (markers)
marker_width = 0.6

# Function to interpolate a Gaussian-like curve for the transition state
def interpol_ts(xxx, yyy):
    xx = list(np.linspace(xxx[0], xxx[1], 50))
    prefac = yyy[1] - yyy[0]
    yy = [yyy[0] + prefac * np.sin(0.5 * np.pi * (x - xxx[0]) / (xxx[1] - xxx[0])) for x in xx]
    xx2 = list(np.linspace(xxx[1], xxx[2], 50))
    prefac = yyy[2] - yyy[1]
    yy += [yyy[2] - prefac * np.sin(0.5 * np.pi * (x - xxx[0]) / (xxx[2] - xxx[1])) for x in xx2]
    xx += xx2
    return xx, yy

# Plotting the data
plt.figure(figsize=(8, 3))

# Define transition states for both CeIII and CeIV
ts_ceiii = [3]  # Transition states for CeIII, e.g., [3]
ts_ceiv = [1]   # Transition states for CeIV, e.g., [1]

# Plot horizontal line markers for CeIII energy levels, skip TS
for i in range(len(reaction_coordinate)):
    if i not in ts_ceiii:
        plt.hlines(delta_G_CeIII[i], reaction_coordinate[i] - marker_width / 2, reaction_coordinate[i] + marker_width / 2, color='black', linewidth=3)

# Plot horizontal line markers for CeIV energy levels, skip TS
for i in range(len(reaction_coordinate2)):
    if i not in ts_ceiv:
        plt.hlines(delta_G_CeIV[i], reaction_coordinate2[i] - marker_width / 2, reaction_coordinate2[i] + marker_width / 2, color='gray', linewidth=3)

# Connect CeIII energy levels with dashed lines, except for the specified transition states (TS)
for i in range(1, len(reaction_coordinate)):
    if i in ts_ceiii:  # For TS in CeIII, plot Gaussian curve and a small marker
        xxx = [reaction_coordinate[i-1] + marker_width / 2, reaction_coordinate[i], reaction_coordinate[i+1] - marker_width / 2]
        yyy = [delta_G_CeIII[i-1], delta_G_CeIII[i], delta_G_CeIII[i+1]]
        xx, yy = interpol_ts(xxx, yyy)
        plt.plot(xx, yy, color='black')
        plt.plot(reaction_coordinate[i], delta_G_CeIII[i], 'o', color='black', markersize=0.01)  # Small marker for TS
    elif i - 1 in ts_ceiii:  # Skip plotting the dashed line after the TS marker
        continue
    else:
        plt.plot([reaction_coordinate[i-1] + marker_width / 2, reaction_coordinate[i] - marker_width / 2],
                 [delta_G_CeIII[i-1], delta_G_CeIII[i]], color='black', linestyle='dashed')

# Connect CeIV energy levels with dashed lines, except for the specified transition states (TS)
for i in range(1, len(reaction_coordinate2)):
    if i in ts_ceiv:  # For TS in CeIV, plot Gaussian curve and a small marker
        xxx = [reaction_coordinate2[i-1] + marker_width / 2, reaction_coordinate2[i], reaction_coordinate2[i+1] - marker_width / 2]
        yyy = [delta_G_CeIV[i-1], delta_G_CeIV[i], delta_G_CeIV[i+1]]
        xx, yy = interpol_ts(xxx, yyy)
        plt.plot(xx, yy, color='gray')
        plt.plot(reaction_coordinate2[i], delta_G_CeIV[i], 'o', color='gray', markersize=0.01)  # Small marker for TS
    elif i - 1 in ts_ceiv:  # Skip plotting the dashed line after the TS marker
        continue
    else:
        plt.plot([reaction_coordinate2[i-1] + marker_width / 2, reaction_coordinate2[i] - marker_width / 2],
                 [delta_G_CeIV[i-1], delta_G_CeIV[i]], color='gray', linestyle='dashed')

# Set labels and title
plt.xlabel('Reaction coordinate')
plt.ylabel('∆G [eV]')

# Set y-axis limits
plt.ylim(-0.5, 0.75)

# Add legend manually
plt.plot([], [], color='black', label='Mechanism 1', linewidth=2)
plt.plot([], [], color='gray', label='Mechanism 2', linewidth=2)
plt.legend()

# Remove x-axis numbers
plt.gca().set_xticklabels([])

# Show gridlines
plt.grid(True)

# Show plot
plt.tight_layout()
plt.show()
