# Documentation: Text-to-Video Generator Web App

## Overview
This project provides a web interface for generating videos from text prompts using a diffusion model. The backend is powered by Flask and HuggingFace Diffusers, while the frontend is a simple HTML/CSS/JS app.

---

## Backend (Flask API)

### Endpoints

#### `/` (GET)
- **Description:** Serves the main HTML page.
- **Returns:** `index.html`

#### `/generate` (POST)
- **Description:** Accepts a text prompt, generates a video, and returns the video URL.
- **Request:**
  - `Content-Type: application/x-www-form-urlencoded`
  - `prompt` (string): The text prompt for video generation.
- **Response:**
  - `200 OK` with JSON: `{ "video_url": "/static/filename.mp4" }`
  - `400 Bad Request` with JSON: `{ "error": "No prompt provided" }`

#### Static Files
- CSS and JS are served from `/static/`.
- Videos are saved and served from `/static/`.

---

## Frontend
- **index.html**: Contains a form for entering the prompt and a video display area.
- **style.css**: Styles the page for a clean, modern look.
- **script.js**: Handles form submission, shows loading, and displays the generated video.

### User Flow
1. User enters a prompt and submits the form.
2. JavaScript sends the prompt to `/generate` via POST.
3. Backend generates the video and returns the video URL.
4. JavaScript displays the video in the browser.

---

## Backend Logic
- Loads the diffusion model once at startup for efficiency.
- On `/generate`, runs inference, saves the video, and returns its URL.
- Moves generated videos to `static/` for serving.

---

## Customization & Extensions
- You can change the model or inference parameters in `app.py`.
- Add authentication, progress bars, or video cleanup as needed.

---

## Troubleshooting
- Ensure you have a CUDA-capable GPU for reasonable performance.
- The first run may be slow due to model download.
- Check Python and package versions if you encounter errors. 