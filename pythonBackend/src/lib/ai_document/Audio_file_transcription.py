import time
from fastapi import UploadFile
import gc
import torch
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline


def audio_file_transcription(audio_path: str):
    start_time = time.time()
    device = "cuda:0" if torch.cuda.is_available() else "cpu"
    torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32

    # Define the directory to save the model locally
    local_model_dir = "./whisper-large-v3-turbo"

    # Download the model and processor locally if not already done
    model_id = "openai/whisper-large-v3-turbo"

    try:
        # Load from local directory if available
        model = AutoModelForSpeechSeq2Seq.from_pretrained(
            local_model_dir,
            torch_dtype=torch_dtype,
            low_cpu_mem_usage=True,
            attn_implementation="flash_attention_2",
        )
        processor = AutoProcessor.from_pretrained(local_model_dir)
        print("Loaded model and processor from local directory.")
    except:
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
        print("Downloaded and saved model and processor locally.")

    model.to(device)

    pipe = pipeline(
        "automatic-speech-recognition",
        model=model,
        tokenizer=processor.tokenizer,
        feature_extractor=processor.feature_extractor,
        chunk_length_s=30,
        batch_size=16,  # batch size for inference - set based on your device
        torch_dtype=torch_dtype,
        device=device,
    )
    result = pipe(audio_path, generate_kwargs={"language": "french"})
    end_time = time.time()
    exec_time = end_time - start_time
    print("Execution time for transcription:", exec_time)

    # Explicit cleanup
    del pipe
    del model
    del processor
    torch.cuda.empty_cache()
    torch.cuda.synchronize()  # Synchronize CUDA operations to ensure completion
    gc.collect()

    return result["text"]
