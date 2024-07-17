from diffusers import StableDiffusionPipeline
import torch

model_id = "SG161222/Realistic_Vision_V6.0_B1_noVAE"

# Load the model
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe = pipe.to("cuda")  # Move the model to the GPU

# Generate an image from text
prompt = "A beautiful landscape with mountains and a river"
image = pipe(prompt).images[0]

# Save the generated image
image.save("generated_image.png")
