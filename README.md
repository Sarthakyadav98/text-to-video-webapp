# Text-to-Video Generator Web App

This project provides a simple web interface to generate videos from text prompts using the `ali-vilab/text-to-video-ms-1.7b` model via HuggingFace Diffusers.

## Features
- Enter a text prompt and generate a video using state-of-the-art diffusion models.
- Simple, modern web interface.
- Python backend (Flask) for model inference.

## Requirements
- Python 3.8+
- pip
- [diffusers](https://github.com/huggingface/diffusers)
- [transformers](https://github.com/huggingface/transformers)
- [accelerate](https://github.com/huggingface/accelerate)
- [Flask](https://flask.palletsprojects.com/)
- CUDA-capable GPU recommended for performance

## Installation
1. Clone the repository:
   ```sh
   git clone <your-repo-url>
   cd <your-repo-directory>
   ```
2. Install dependencies:
   ```sh
   pip install flask diffusers transformers accelerate
   ```

## Usage
1. Start the Flask server:
   ```sh
   python app.py
   ```
2. Open your browser and go to [http://localhost:5000](http://localhost:5000)
3. Enter a prompt and generate a video!

## Project Structure
```
Program/
  app.py                # Flask backend
  backendScript.py      # Original script (reference)
  static/
    style.css           # CSS for frontend
    script.js           # JavaScript for frontend
  templates/
    index.html          # HTML frontend
```

## Notes
- The first model load may take a while as it downloads weights.
- Generated videos are saved in the `static/` directory for serving.
- For production, consider using a more robust server and cleaning up old video files.

## License
MIT (or specify your license) 