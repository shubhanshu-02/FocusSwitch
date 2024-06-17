# Gaze Control Project

This project uses a webcam to detect which monitor a user is looking at and redirects keyboard input accordingly.

## Setup Instructions

1. Clone the repository.
2. Install the required packages using `pip install -r requirements.txt`.
3. Download the pre-trained model file `shape_predictor_68_face_landmarks.dat` and place it in the `data/` directory.
4. Run the project using `python src/main.py`.

## Project Structure

- `data/`: Contains the pre-trained model file.
- `src/`: Contains all the source code files.
- `requirements.txt`: Lists all the dependencies required for the project.
- `README.md`: Provides an overview of the project and instructions.

## Running the Project

```bash
python src/main.py
