<!-- @format -->

# gTTS with CORS Support

This Docker image provides a text-to-speech (TTS) service using `gTTS` (Google Text-to-Speech) with added CORS support for cross-origin requests. It’s a modified version of the original `hirotakakato/gtts` image, enhanced with `flask-cors` to enable usage in web applications like Next.js. The service runs on a Flask app with Gunicorn for production-ready performance.

## Overview

This image is designed for applications needing text-to-speech functionality, particularly for Thai language support (`lang=th`). It addresses CORS issues by including the `Access-Control-Allow-Origin: *` header, making it suitable for browser-based applications. The app runs on port `80` inside the container, which is mapped to port `8111` on the host using a Docker bridge network.

## Features

- Converts text to speech in various languages (default: Thai, `lang=th`).
- Supports CORS for cross-origin requests, enabling use in web apps.
- Runs on port `80` inside the container, mapped to `8111` on the host.
- Uses Gunicorn as a production-ready WSGI server.
- Lightweight image based on `python:3.9-slim`.

## Prerequisites

- Docker installed on your system.
- A Docker Hub account to pull the image (optional if building locally).
- For Code Server users: Ensure the proxy path (e.g., `/absproxy/8111`) is configured correctly.

## Usage

Follow these steps to run the `gTTS` service using the Docker image.

### 1. Pull the Image

Pull the image from Docker Hub:

```bash
docker pull <your-username>/gtts-with-cors:latest
```
