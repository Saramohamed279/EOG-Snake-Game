# EOG-Snake-Game

A human-computer interface game based on EOG (Electrooculography) signals. This project combines machine learning and real-time signal processing to control a snake game using eye movements.

## 📋 Project Description

This repository implements an innovative approach to game control using EOG (Electrooculography), a non-invasive technique that measures the corneal-retinal potential to track eye movements. Players can control the classic Snake game using their eye gaze direction instead of traditional keyboard inputs.

## 🎮 Game Features

- **EOG-based Control**: Control the snake using eye movements
- **Real-time Processing**: Live signal processing from EOG sensors
- **Snake Gameplay**: Classic snake and apple game mechanics
- **Machine Learning Integration**: Eye movement classification and recognition

## 📊 Technology Stack

- **Jupyter Notebook** (99.9%) - Data analysis and interactive development
- **Python** (0.1%) - Supporting utilities and backend logic
- **Key Libraries**: 
  - Signal Processing: scipy, numpy
  - Machine Learning: scikit-learn
  - Visualization: matplotlib, pygame

## 📈 Dataset

The project uses EOG signal data for training and testing. Access the dataset here:
[EOG Signal Dataset](https://drive.google.com/file/d/1MXYcNlrx43ngU6HEaNoGNIyLDNWwl4D3/view?usp=share_link)

## 🚀 Getting Started

### Prerequisites
- Python 3.7+
- Jupyter Notebook
- Required libraries (see requirements.txt or environment.yml)

### Installation

```bash
# Clone the repository
git clone https://github.com/Saramohamed279/EOG-Snake-Game.git
cd EOG-Snake-Game

# Install dependencies
pip install -r requirements.txt
```

### Usage

1. Open the Jupyter Notebooks in the repository
2. Run the data processing and model training notebooks
3. Launch the game interface to play using EOG signals

## 📁 Project Structure

```
EOG-Snake-Game/
├── README.md
├── game/
│   └── [Game implementation files]
├── notebooks/
│   └── [Jupyter notebooks for analysis and training]
└── data/
    └── [Dataset and preprocessing scripts]
```

## 🎯 How It Works

1. **Signal Acquisition**: EOG signals are captured from the user
2. **Preprocessing**: Raw signals are filtered and normalized
3. **Feature Extraction**: Relevant features for eye movement are extracted
4. **Classification**: Machine learning model predicts eye gaze direction
5. **Game Control**: Predicted direction controls the snake movement

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any improvements or bug reports.

## 📝 License

This project is open source and available under the MIT License.

## 👤 Author

**Saramohamed279**

## 🔗 References

- [EOG Technology Overview](https://en.wikipedia.org/wiki/Electrooculography)
- Pygame Documentation: https://www.pygame.org/
- Scikit-learn: https://scikit-learn.org/

---

For questions or support, please open an issue in the repository.
