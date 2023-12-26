# ByteBabble

This is a simple chat application built using FastAPI, MongoDB, and WebSockets.

## Features

- Real-time messaging using WebSockets
- User authentication and registration
- Messages stored in MongoDB for persistent storage
- RESTful API for basic chat functionality

## Technologies Used

- [FastAPI](https://fastapi.tiangolo.com/): FastAPI is a modern, fast web framework for building APIs with Python 3.7+ based on standard Python type hints.
- [MongoDB](https://www.mongodb.com/): MongoDB is a NoSQL database for storing chat messages.
- [WebSockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API): WebSockets provide full-duplex communication channels over a single TCP connection.

## Setup

### Prerequisites

- Python 3.7+
- MongoDB installed and running

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/ByteBabble.git
    cd fastapi-chat-app
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up MongoDB:
    - Install MongoDB locally or use a remote MongoDB instance.
    - Update the MongoDB connection string in `app/core/config.py` (if required).

5. Run the FastAPI application:

    ```bash
    uvicorn main:app --reload
    ```

6. Open your browser and go to `http://127.0.0.1:8000/docs` for Swagger documentation and API testing.

## Contributing

Feel free to contribute to the development of this chat app by creating issues or pull requests. Your feedback and contributions are highly appreciated!
