import asyncio
import websockets
from src.asr.asr_factory import ASRFactory
import json
import logging

logging.basicConfig(level=logging.INFO)

async def handle_client(websocket, path):
	asr_pipeline = ASRFactory.create_asr_pipeline("faster_whisper", model_size="large-v3")
	try:
		while True:
			message = await websocket.recv()
			logging.info(f"Message received: {message}")
			if message is None:
				logging.info("No message received")
				break

			# Assuming message is binary audio data
			transcription = await asr_pipeline.transcribe(message)
			logging.info(f"Transcription: {transcription}")
			await websocket.send(json.dumps(transcription))
			logging.info(f"Transcription sent: {transcription}")
	except websockets.exceptions.ConnectionClosed:
		print("Connection with client closed")

# Start the server
async def main():
    logging.info("Starting server")
    async with websockets.serve(handle_client, '0.0.0.0', 8765):
        await asyncio.Future()  # Run forever

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("Server stopped by user")
