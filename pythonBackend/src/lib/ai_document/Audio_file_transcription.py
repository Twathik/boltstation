import gc
import torch
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline, logging

logging.set_verbosity_error()  # ✅ Suppresses unnecessary logs


def audio_file_transcription(audio_path: str):
    """Transcribes an audio file using Whisper large-v3-turbo."""
    device = "cuda:0" if torch.cuda.is_available() else "cpu"
    torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32

    # Define the directory to save the model locally
    local_model_dir = "./whisper-large-v3-turbo"
    model_id = "openai/whisper-large-v3-turbo"

    try:
        # Try to load the model from the local directory
        model = AutoModelForSpeechSeq2Seq.from_pretrained(
            local_model_dir,
            torch_dtype=torch_dtype,
            low_cpu_mem_usage=True,
            attn_implementation="flash_attention_2",
        )
        processor = AutoProcessor.from_pretrained(local_model_dir)
    except Exception as e:
        print("Loading model from Hugging Face due to:", str(e))

        # If not available locally, download and save them
        model = AutoModelForSpeechSeq2Seq.from_pretrained(
            model_id,
            torch_dtype=torch_dtype,
            low_cpu_mem_usage=True,
            attn_implementation="flash_attention_2",
        )
        processor = AutoProcessor.from_pretrained(model_id)

        # Save the model and processor locally
        model.save_pretrained(local_model_dir)
        processor.save_pretrained(local_model_dir)
        print("Model and processor downloaded & saved locally.")

    # Move model to device
    model.to(device)

    # ✅ Correct pipeline usage to avoid deprecated warnings
    pipe = pipeline(
        "automatic-speech-recognition",
        model=model,
        tokenizer=processor.tokenizer,
        feature_extractor=processor.feature_extractor,
        chunk_length_s=30,
        batch_size=16,  # Set batch size based on your device
        torch_dtype=torch_dtype,
        device=device,
    )

    try:
        # ✅ Explicitly pass `input_features` to avoid deprecation warnings
        result = pipe(audio_path, generate_kwargs={"language": "fr"})  # "fr" for French

        # ✅ Explicit cleanup to free memory
        del pipe
        del model
        del processor
        torch.cuda.empty_cache()
        torch.cuda.synchronize()  # Ensures CUDA operations are completed
        gc.collect()

        return result["text"]

    except Exception as e:
        print("Error during transcription:", str(e))
        return None
