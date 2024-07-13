## Sample CRUD app

   - Flask application with CRUD operations for managing a players collection in MongoDB

     ### Explanation of the Flow
    
      1. **app.py**: The main application file where the Flask app is created. It loads environment variables and registers the routes from `player_routes.py`.

      2. **routes/player_routes.py**: Defines the routes for the CRUD operations. It uses a Blueprint to organize routes related to the player resource.

      3. **controllers/player_controller.py**: Contains the logic for the CRUD operations. It connects to MongoDB, performs operations, and returns responses.

      4. **controllers/memory_controller.py**: This setup provides an alternative set of CRUD operations that do not require a database, using an in-memory dictionary for storage.

---------------------------------------

## Running the Application and Tests

1. Install required packages:

    ```bash
    sudo apt-get update && sudo apt-get install python3 python3-pip -y 
    pip3 install flask pymongo flask-pymongo python-dotenv pytest pytest-cov coverage venv
    ```

1. Create and Activate Venv
    
    ```bash
    ### 1.1) Create a Virtual Environment
    python -m venv devenv
       ## OR 
    virtualenv devenv

    ### 1.2) Activate the Virtual Environment
    # On Windows:
    devenv\Scripts\activate
   
    # On macOS/Linux:
    source devenv/bin/activate

    # save required package in req.txt
    pip freeze > req.txt

    # When you are done, you can deactivate the virtual environment by simply running:
    deactivate
    ```

1. **Run MongoDB Container**:

   ```bash
   docker run -d --name mongodb -p 27017:27017 -e MONGO_INITDB_ROOT_USERNAME=myusername \
   -e MONGO_INITDB_ROOT_PASSWORD=mypassword mongo:latest

   docker stop mongodb
   ```


2. Run the Flask application:
    
    ```bash
    # Install packages
    pip install -r req.txt
    python app.py
    ```
---------------------------------------------


## Running Tests and Generating Coverage Report

1. Run only Unit tests

    ```bash
    export PYTHONPATH=$(pwd)
    pytest
    ```

1. **Run the Tests with Coverage**:

   ```bash
   coverage run -m unittest discover -s tests
   ```

    - -m unittest discover discovers and runs all tests in the tests directory.

1. **Generate the Coverage Report**:

   ```bash
   coverage report -m
   ```
     - coverage report` generates a textual report

    - `-m` shows the missing lines of code.

1. **Generate an HTML Coverage Report**:

   ```bash
   coverage html
   ```
   This will create an `htmlcov` directory with the HTML report. Open `htmlcov/index.html` in a web browser to view the coverage details.

4. **Coverage Explanation**

   - Coverage measures how much of your code is exercised when running your tests. 
    
      This helps identify parts of the code that are not tested, ensuring better quality and reliability of the codebase.

        1. **Line Coverage**: Indicates the percentage of code lines executed during tests.
     
        1. **Branch Coverage**: Shows the percentage of code branches (e.g., `if` statements) executed.
     
        1. **Missing Lines**: Lists lines of code not executed during tests.

       Using coverage reports, you can improve your tests to cover more scenarios, resulting in more robust and error-free applications.   


-----------------------------------------

## Running the Flask App with Docker

1. **Build the Docker Image**:

   ```bash
   docker build -t my_flask_app .
   ```

2. **Run the Flask App Container**:

   ```bash
   docker run -d --name flask_app -p 5000:5000 --env MONGO_URL=mongodb://myusername:mypassword@host.docker.internal:27017/mydatabase my_flask_app
   ```

-------------------------------

## Sample curl Requests

1. **Create a Player**

    ```bash
    curl -X POST http://127.0.0.1:5000/api/player \
    -H "Content-Type: application/json" \
    -d '{
        "name": "Lionel Messi",
        "matches": 900,
        "goals": 860,
        "assists": 900,
        "club": "Inter Miami",
        "age": 40,
        "country": "Argentina"
    }'
    ```

2. **Get All Players**

    ```bash
    curl -X GET http://127.0.0.1:5000/api/players
    curl -X GET http://127.0.0.1:5000/memory/players
    ```

1. **Get a Single Player**

    ```bash
    curl -X GET http://127.0.0.1:5000/api/player/<player_id>
    ```
    Replace `<player_id>` with the actual player ID.

1. **Update a Player**

    ```bash
    curl -X PUT http://127.0.0.1:5000/api/player/<player_id> \
    -H "Content-Type: application/json" \
    -d '{
        "name": "Lionel Messi",
        "matches": 910,
        "goals": 870,
        "assists": 910,
        "club": "Inter Miami",
        "age": 41,
        "country": "Argentina"
    }'
    ```
    Replace `<player_id>` with the actual player ID.

1. **Delete a Player**

    ```bash
    curl -X DELETE http://127.0.0.1:5000/api/player/<player_id>
    ```
    Replace `<player_id>` with the actual player ID.

    This setup provides a well-structured foundation for CRUD operations on a `players` collection in MongoDB using Flask.

----------------------------------------------

## Test Code Explanation

### Test for MongoDB-based CRUD Operations (`test_player_controller.py`)

1. **Imports and Setup**:
   
    ```python
    import unittest
    from unittest.mock import patch
    from app import app
    ```
    - `unittest` is the Python unit testing framework.
    - `unittest.mock.patch` is used to mock the `collection` object to simulate database operations.
    - `app` is imported from our Flask application to create test clients.

2. **Test Class**:
    
      This class contains all test cases for the MongoDB-based CRUD operations. It inherits from `unittest.TestCase`.

      ```python
      class TestPlayerController(unittest.TestCase):
      ```

3. **Mocking the Collection**:
     
    - `@patch` replaces the actual `collection` object in the `player_controller` with a mock object, allowing us to simulate database responses.
    
        ```python
        @patch('controllers.player_controller.collection')
        ```

4. **Test Cases**:

    - **`test_get_all_players`**:

      Simulates a call to `collection.find` and verifies the response of the `GET /api/players` endpoint.

         ```python
         def test_get_all_players(self, mock_collection):
             mock_collection.find.return_value = [...]
             with app.test_client() as client:
                 response = client.get('/api/players')
                 self.assertEqual(response.status_code, 200)
                 self.assertEqual(len(response.json), 1)
                 self.assertEqual(response.json[0]['name'], 'Lionel Messi')
         ```

    - **`test_create_player`**:
      
       Simulates inserting a new player and verifies the response of the `POST /api/player` endpoint.
      
         ```python
         def test_create_player(self, mock_collection):
             mock_collection.insert_one.return_value.inserted_id = '60c72b2f4f1a2567f8d6b6c0'
             with app.test_client() as client:
                 response = client.post('/api/player', json={...})
                 self.assertEqual(response.status_code, 201)
                 self.assertEqual(response.json['_id'], '60c72b2f4f1a2567f8d6b6c0')
         ```


---------------------------------

### Test for In-memory CRUD Operations (`test_memory_controller.py`)

1. **Imports and Setup**:
    
    Similar to the MongoDB-based tests, but also imports `players_memory` to manipulate the in-memory data.
    
    ```python
    import unittest
    from app import app
    from controllers.memory_controller import players_memory
    ```
    

2. **Test Class**:
    
    Contains all test cases for in-memory CRUD operations.
    
    ```python
    class TestMemoryController(unittest.TestCase):
    ```

3. **Setup Method**:
    
    Clears the in-memory data before each test to ensure a clean state.
    
    ```python
    def setUp(self):
        players_memory.clear()
        self.client = app.test_client()
    ```

4. **Test Cases**:
    
    - **`test_get_all_players_memory`**:
      
      Adds a player to `players_memory` and verifies the response of the `GET /memory/players` endpoint.
      
      
      ```python
      def test_get_all_players_memory(self):
          players_memory['1'] = {...}
          response = self.client.get('/memory/players')
          self.assertEqual(response.status_code, 200)
          self.assertEqual(len(response.json), 1)
          self.assertEqual(response.json[0]['name'], 'Lionel Messi')
      ```


    - **`test_update_player_memory`**:
      
      Updates an existing player in-memory and verifies the response of the `PUT /memory/player/<player_id>` endpoint.
      
      ```python
      def test_update_player_memory(self):
          player_id = '1'
          players_memory[player_id] = {...}
          response = self.client.put(f'/memory/player/{player_id}', json={...})
          self.assertEqual(response.status_code, 200)
          self.assertEqual(players_memory[player_id]['matches'], 910)
      ```
----------------------------

## Basic Pytest Usage

### Basic Usage

1. **Run all tests in the current directory and subdirectories**:
   
   ```bash
   pytest

   # Run tests and show print statements (stdout)
   pytest -s
   ```

2. **Run tests in a specific file**:
   
   ```bash
   pytest path/to/test_file.py
   ```

3. **Run a specific test function**:
   
   ```bash
   pytest path/to/test_file.py::test_function_name
   ```

1. **Run tests matching a specific substring in their name**:

   ```bash
   pytest -k "substring"
   # Run tests that match a given expression
   pytest -k "expression"
   ```

1. **Run tests and stop on the first error or failure**:
   
   ```bash
   pytest -x

   # Run tests and stop after the first N failures
   pytest --maxfail=N
   ```

   --------------------

### Output Options

1. **Show detailed test execution summary**:
   
   ```bash
   pytest -v

   # Show only the summary of test results (quiet mode)
   pytest -q
   ```

1. **Generate JUnit XML report for CI integration**:
  
   ```bash
   pytest --junitxml=path/to/output.xml
   ```

1. **Run tests with coverage report**:
  
   ```bash
   pytest --cov=path/to/module_or_package
   ```

2. **Generate HTML coverage report**:
  
   ```bash
   pytest --cov=path/to/module_or_package --cov-report=html
   ```
   
   --------------------

### Running Tests in Parallel

1. **Run tests in parallel processes**:
   ```bash
   pytest -n auto
   ```

2. **Run tests in parallel on multiple cores (N cores)**:
   ```bash
   pytest -n N
   ```
   --------------------

### Running Tests with Custom Configuration

1. **Use a custom configuration file (pytest.ini)**:
   
   ```bash
   pytest -c path/to/pytest.ini
   ```

2. **Run tests with custom command-line options**:
   
   ```bash
   pytest --options=value
   ```

--------------------