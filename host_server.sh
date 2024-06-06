source VoiceStreamAI/bin/activate
python3 -m src.main --host 0.0.0.0 --certfile certs/fullchain1.pem --keyfile certs/privkey1.pem --asr-args '{"model_size": "large-v3"}'