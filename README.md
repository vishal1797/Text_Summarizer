# Text Summarization using Pegasus Model

This project demonstrates text summarization using the Pegasus model through a Flask web application.

## Features

- Summarize input text using the Pegasus model.
- User-friendly web interface for input and output.

## Requirements

- Python 3.8 or higher
- Docker (optional, for containerization)

## Installation

1. Clone the repository:

```
git clone https://github.com/your_username/your_project.git
cd your_project
```

2. Install dependencies:

```
pip install -r requirements.txt
```

## Usage

### Running the Flask application locally

1. Navigate to the project directory:

```
cd path/to/your_project
```

2. Run the Flask application:

```
python app.py
```

3. Open a web browser and go to `http://localhost:5000` to access the application.

### Running the Flask application using Docker

1. Build the Docker image:

```
docker build -t summarization-app .
```

2. Run the Docker container:

```
docker run -p 5000:5000 summarization-app
```

3. Open a web browser and go to `http://localhost:5000` to access the application.

## Project Directory Structure

```
project_folder/
│
├── app.py
├── Dockerfile
├── requirements.txt
└── templates/
    └── index.html
```

## How it works

- The Flask application provides a form where users can input text.
- Upon submission, the input text is sent to the Pegasus model for summarization.
- The summarized text is displayed to the user.

## Files and directories

- `app.py`: Flask application script.
- `templates/index.html`: HTML template for the web interface.
- `requirements.txt`: List of Python dependencies.
- `Dockerfile`: Docker configuration file for containerization.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

