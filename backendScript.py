# %%
# !pip install diffusers transformers accelerate

# %%
import torch
from diffusers import DiffusionPipeline, DPMSolverMultistepScheduler
from diffusers.utils import export_to_video

pipe = DiffusionPipeline.from_pretrained("ali-vilab/text-to-video-ms-1.7b",torch_dtype=torch.float16, variant="fp16")
pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)
# If you do not have gpu comment out the line below
pipe.enable_model_cpu_offload()

# %%
import numpy as np

prompt = "A bear is dance"

# Get the frames AND remove the extra 'batch' dimension by selecting the first element [0]
video_frames_tensor = pipe(prompt, num_inference_steps=50).frames[0]

# Now, convert the correctly shaped tensor to the uint8 format
video_frames_uint8 = (video_frames_tensor * 255).astype(np.uint8)

# Export the correctly formatted frames
video_path = export_to_video(video_frames_uint8)
video_name = video_path.replace('/tmp/', '')
print('Name:', video_name)


