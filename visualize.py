import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.patches as patches
from typing import List, Tuple
import os

def create_visualization(grid: np.ndarray, 
                        tom_positions: List[Tuple[int, int]],
                        jerry_positions: List[Tuple[int, int]],
                        spike_positions: List[Tuple[int, int]],
                        output_file: str = 'visualization.gif'):
    """
    Creates an animated visualization of agent movements.
    
    Args:
        grid: 2D numpy array representing the environment
        tom_positions: List of Tom's positions over time
        jerry_positions: List of Jerry's positions over time
        spike_positions: List of Spike's positions over time
        output_file: Name of the output GIF file
    """
    fig, ax = plt.subplots(figsize=(10, 10))
    
    # Plot grid
    ax.imshow(grid, cmap='Greys', alpha=0.3)
    
    # Create patches for agents
    tom_patch = patches.Circle((0, 0), 0.3, color='red', label='Tom')
    jerry_patch = patches.Circle((0, 0), 0.3, color='blue', label='Jerry')
    spike_patch = patches.Circle((0, 0), 0.3, color='green', label='Spike')
    
    ax.add_patch(tom_patch)
    ax.add_patch(jerry_patch)
    ax.add_patch(spike_patch)
    
    # Add legend
    ax.legend()
    
    def update(frame):
        # Update agent positions
        tom_patch.center = (tom_positions[frame][1], tom_positions[frame][0])
        jerry_patch.center = (jerry_positions[frame][1], jerry_positions[frame][0])
        spike_patch.center = (spike_positions[frame][1], spike_positions[frame][0])
        
        # Add title with frame number
        ax.set_title(f'Frame {frame + 1}')
        
        return tom_patch, jerry_patch, spike_patch
    
    # Create animation
    anim = FuncAnimation(fig, update, frames=len(tom_positions),
                        interval=200, blit=True)
    
    # Save animation
    anim.save(output_file, writer='pillow', fps=5)
    plt.close()

def generate_sample_visualization():
    """Generate a sample visualization for demonstration."""
    # Create a sample grid
    grid = np.zeros((10, 10))
    grid[3:7, 3:7] = 1  # Add some obstacles
    
    # Create sample movement patterns
    n_frames = 20
    tom_positions = [(i, i) for i in range(n_frames)]
    jerry_positions = [(i, 9-i) for i in range(n_frames)]
    spike_positions = [(9-i, i) for i in range(n_frames)]
    
    # Create visualization
    create_visualization(grid, tom_positions, jerry_positions, spike_positions)

if __name__ == "__main__":
    generate_sample_visualization() 