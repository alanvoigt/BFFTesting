# BFF (Backend For Frontend) with Flask

This project consists of a simple implementation of a BFF (Backend For Frontend) using Flask. The BFF integrates with two microservices: one for retrieving user information and another for fetching order data. The goal is to aggregate data from both microservices and serve a unified response for the frontend.

## Project Structure

The project is composed of three main parts:

1. **BFF (`app.py`)**: The BFF is responsible for aggregating data from different microservices and serving a single endpoint for the frontend.
2. **User Service (`Service1.py`)**: Microservice simulating user data retrieval.
3. **Order Service (`Service2.py`)**: Microservice simulating order data retrieval.
4. **Tests**: Integration tests ensuring that the BFF correctly combines data from the microservices.

## Dependencies

This project uses the following dependencies:

- **Flask**: Framework to build the BFF and microservices.
- **requests**: Library to make HTTP calls between services.
- **pytest**: Framework for testing the integration between services.

## Running the Project

1. **Start the Services**
   You need to run the three services on their respective ports so that the BFF can interact with them:

User Service (port 5001): Service returning user data.

```bash
python Service1.py
```

Order Service (port 5002): Service returning order data.

```bash
python Service2.py
```

BFF (port 5000): The BFF that aggregates data from both microservices.

```bash
python app.py
```

2. Running the Tests
   To test the integration between the microservices and the BFF, run the following command:

```bash
pytest test/test_bff_integration.py -v
```

The tests will check if the BFF is correctly aggregating data from both the user and order services.

To install dependencies, run:

```bash
pip install -r requirements.txt
```
