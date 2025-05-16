# 🏃‍♂️ Multi-Agent Pursue-Escape Simulation

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-Active-success)]()

## 📋 Overview

This project implements a real-time multi-agent pursuit-evasion system featuring three intelligent agents: Tom, Jerry, and Spike. The system demonstrates sophisticated path planning and decision-making algorithms in a dynamic, adversarial environment with real-time visualization.

### 🎯 Key Features
- Real-time agent movement visualization
- Dynamic obstacle avoidance
- Competitive multi-agent interactions
- Automatic simulation progression
- Step-by-step movement tracking

### 🤖 Agent Roles
- **Tom** (Red): Pursues Jerry while evading Spike
- **Jerry** (Blue): Pursues Spike while evading Tom
- **Spike** (Green): Pursues Tom while evading Jerry

## 🏗️ Project Structure
```
project_root/
│── data/                # Grid environments and initial positions
│   ├── grid_files/     # Grid environment files
│   └── proj_ii_solutions/ # Solution logs
│── main.py             # Core simulation engine with visualization
│── planners/           # Agent planning algorithms
│   ├── planner_tom.py  # Tom's planning logic
│   ├── planner_jerry.py# Jerry's planning logic
│   └── planner_spike.py# Spike's planning logic
│── devel.py            # Development and testing utilities
│── README.md           # Project documentation
```

## 🎮 Simulation Features

### Visualization
- Real-time display of agent movements
- Color-coded agents (Tom: Red, Jerry: Blue, Spike: Green)
- Grid environment with obstacle representation
- Step counter and task information
- Automatic progression with configurable delay

### Scoring System
- **3 points**: Awarded to the winning agent (successful capture)
- **0 points**: Awarded to losing agents
- **1 point each**: Awarded in case of a tie

### Termination Conditions
- Successful capture of target
- Collision with obstacles
- Maximum step limit reached

## 💻 Implementation Details

### Core Components

#### `main.py`
- Simulation orchestration
- Real-time visualization
- Environment management
- Turn-based execution
- Result logging

#### Visualization Features
```python
def setup_visualization(self):
    """Setup the visualization window with:
    - Grid environment display
    - Agent position markers
    - Status information
    - Automatic updates
    """
```

### Dependencies
- Python 3.8+
- NumPy
- Matplotlib
- Pandas

### Installation
```bash
# Clone the repository
git clone https://github.com/yourusername/pursue-escape-planning.git

# Navigate to project directory
cd pursue-escape-planning

# Run the simulation
python main.py
```

## 📊 Performance

The system has been tested across 100 different task configurations, demonstrating:
- Efficient path planning
- Successful target capture
- Effective obstacle avoidance
- Dynamic decision making

## 🛠️ Development

### Testing
- Use `devel.py` for development and testing
- Each task is tested 5 times for reliability
- Results are logged in CSV format

### Customization
- Adjust `step_delay` in `main.py` to control animation speed
- Modify agent colors and sizes in visualization
- Customize grid environments in `data/grid_files/`

## 📝 License

This project is licensed under the MIT License.

## 👥 Authors

- Your Name - Initial work

## 🙏 Acknowledgments

- Thanks to all contributors
- Inspired by classic pursuit-evasion problems
- Built with modern AI/ML techniques
