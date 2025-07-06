from flask import Flask, request, send_file, render_template
import os
import torch
from diffusers import DiffusionPipeline, DPMSolverMultistepScheduler
from diffusers.utils import export_to_video
import numpy as np

app = Flask(__name__, static_folder='static', template_folder='templates')

# Load the model once at startup
pipe = DiffusionPipeline.from_pretrained("ali-vilab/text-to-video-ms-1.7b", torch_dtype=torch.float16, variant="fp16")
pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)
pipe.enable_model_cpu_offload()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    prompt = request.form.get('prompt')
    if not prompt:
        return {'error': 'No prompt provided'}, 400
    video_frames_tensor = pipe(prompt, num_inference_steps=50).frames[0]
    video_frames_uint8 = (video_frames_tensor * 255).astype(np.uint8)
    video_path = export_to_video(video_frames_uint8)
    # Move video to static folder for serving
    output_path = os.path.join('static', os.path.basename(video_path))
    os.rename(video_path, output_path)
    return {'video_url': f'/static/{os.path.basename(video_path)}'}

if __name__ == '__main__':
    app.run(debug=True) 