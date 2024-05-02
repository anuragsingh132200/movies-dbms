Sure, here's a README template for the assignment:

---

# Movie Database Backend

This project is a simple backend API for managing a movie database built using Flask and SQLite. It provides endpoints for fetching, adding, updating movies, as well as deleting actors if they are not associated with any movies.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository_url>
   ```

2. Navigate to the project directory:
   ```bash
   cd movie_database
   ```

3. Create a virtual environment:
   ```bash
   python3 -m venv venv
   ```

4. Activate the virtual environment:
   - On Linux/Mac:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

5. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

6. Set up the database:
   ```bash
   flask db upgrade
   ```

## Usage

1. Run the Flask application:
   ```bash
   python run.py
   ```

2. Access the API endpoints using a REST client or tools like `curl` or `Postman`.

## API Endpoints

- **GET /movies**: Fetch all movies with pagination and custom filters.
  - Parameters:
    - `page`: Page number (default: 1)
    - `per_page`: Movies per page (default: 10)
    - `actor_name`: Filter movies by actor name
    - `director_name`: Filter movies by director name

- **GET /movies/<int:id>**: Fetch a specific movie by ID.

- **POST /movies**: Add a new movie.
  - Request body should contain JSON data with keys `name`, `year`, and `ratings`.

- **POST /movies/<int:id>**: Update a movie by ID.
  - Request body should contain JSON data with optional keys `name`, `year`, and `ratings`.

- **POST /actors/<int:id>**: Delete an actor by ID if not associated with any movies.

## Contributing

Contributions are welcome! Feel free to open issues or pull requests for any improvements or feature requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

You can customize this README template further based on your project's specific requirements or additional instructions.