Below is a detailed `README.md` file for your project:

```markdown
# NA Expense Service

## Description

NA Expense Service is a FastAPI-based web application designed to track expenses. It allows users to log expenses via a simple web interface and stores the data in a Google Sheets document. The application uses Google Sheets API for data storage and retrieval.

---

## Features

- **Expense Logging**: Users can log expenses with details like date, name, category, priority, and amount.
- **Google Sheets Integration**: Expenses are stored in a Google Sheets document for easy access and management.
- **Responsive Design**: The web interface is styled for both light and dark modes.

---

## Requirements

### System Requirements
- Python >= 3.9, < 4.0
- Internet connection (for Google Sheets API)

### Python Dependencies
The application uses the following Python libraries:
- `fastapi`
- `uvicorn`
- `jinja2`
- `openpyxl`
- `gspread`
- `google-auth`
- `google-auth-oauthlib`
- `requests`
- `python-multipart`

Refer to the `pyproject.toml` file for the complete list of dependencies.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/na-expense-service.git
   cd na-expense-service
   ```

2. Install dependencies using Poetry:
   ```bash
   poetry install
   ```

3. Activate the virtual environment:
   ```bash
   poetry shell
   ```

---

## Configuration

1. **Google Service Account Credentials**:
   - Place your `service_account.json` file in the `creds/` directory.
   - Ensure the file contains valid credentials for accessing Google Sheets.

2. **Constants**:
   - Update `app/constants.py` with the correct spreadsheet name, worksheet name, and other configurations.

---

## Running the Application

1. Start the FastAPI server using Uvicorn:
   ```bash
   uvicorn main:app --reload
   ```

2. Open your browser and navigate to:
   ```
   http://127.0.0.1:8000/
   ```

---

## Usage

1. **Log an Expense**:
   - Fill out the form on the homepage with details like date, name, category, priority, and amount.
   - Click "Submit" to save the expense to Google Sheets.

2. **View Saved Expenses**:
   - Open the linked Google Sheets document to view all logged expenses.

---

## Project Structure

```
na-expense-service/
├── app/
│   ├── constants.py
├── creds/
│   ├── service_account.json
├── static/
│   ├── style.css
├── templates/
│   ├── index.html
├── main.py
├── pyproject.toml
├── README.md
```

---

## License

This project is licensed under the MIT License.

---

## Author

Created by Naman Singh (<nnaman33@gmail.com>).
