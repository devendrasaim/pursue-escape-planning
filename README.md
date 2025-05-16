# Multi-Agent Pursue-Escape Planning System

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-Active-success)]()
[![License](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

## Project Overview
Implemented a sophisticated multi-agent pursuit-evasion system using Python, featuring three autonomous agents with real-time decision-making capabilities. The system demonstrates advanced path planning algorithms and dynamic obstacle avoidance in a competitive environment.

## Technical Highlights
- **Advanced Path Planning**: Implemented MCTS (Monte Carlo Tree Search) algorithm for optimal path planning
- **Real-time Visualization**: Developed interactive visualization system using Matplotlib
- **Multi-agent Coordination**: Engineered complex agent interactions with pursuit-evasion dynamics
- **Performance Optimization**: Achieved efficient path planning with obstacle avoidance
- **Modular Architecture**: Designed extensible system with separate planning modules for each agent

## Key Features
- Real-time agent movement visualization
- Dynamic obstacle avoidance
- Competitive multi-agent interactions
- Automatic simulation progression
- Step-by-step movement tracking

## Technical Implementation
- **Languages & Tools**: Python, NumPy, Matplotlib, Pandas
- **Algorithms**: MCTS, Path Planning, Dynamic Programming
- **Architecture**: Object-oriented design with modular components
- **Testing**: Comprehensive testing across 100 different scenarios

## Project Structure
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
```

## Performance Metrics
- Successfully tested across 100 different task configurations
- Achieved optimal path planning in complex environments
- Implemented efficient collision detection and avoidance
- Demonstrated robust multi-agent coordination

## Skills Demonstrated
- Advanced Algorithm Implementation
- Real-time System Development
- Multi-agent System Design
- Data Visualization
- Problem-solving and Optimization
- Software Architecture

## Installation & Usage
```bash
# Clone the repository
git clone https://github.com/yourusername/pursue-escape-planning.git

# Navigate to project directory
cd pursue-escape-planning

# Run the simulation
python main.py
```

## Future Enhancements
- Machine Learning integration for improved path planning
- Enhanced visualization capabilities
- Performance optimization for larger environments
- Additional agent types and behaviors

## License
This project is licensed under the MIT License.
