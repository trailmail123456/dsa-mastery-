# Setup and Configuration

This file contains setup instructions and configurations for the DSA Mastery project.

## Environment Setup

### 1. Clone the Repository
```bash
git clone https://github.com/trailmail123456/dsa-mastery-.git
cd dsa-mastery-
```

### 2. Create Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies (Optional - for development)
```bash
pip install -r requirements.txt
```

## Running Code

### Run a Single File
```bash
python3 data_structures/arrays/binary_search.py
```

### Run Tests
```bash
pytest tests/
pytest tests/ -v  # Verbose output
pytest tests/ --cov  # With coverage
```

## IDE Setup

### VS Code
1. Install "Python" extension by Microsoft
2. Install "Pylance" for type checking
3. Create `.vscode/settings.json`:
```json
{
    "python.linting.enabled": true,
    "python.linting.pylintEnabled": true,
    "python.formatting.provider": "black",
    "editor.formatOnSave": true,
    "editor.rulers": [79, 120]
}
```

### PyCharm
1. Open the project
2. Configure Python interpreter: Settings → Project → Python Interpreter
3. Enable code inspection: Settings → Editor → Inspections

## Pre-commit Hooks (Optional)

Create `.git/hooks/pre-commit`:
```bash
#!/bin/bash
black .
flake8 .
pytest tests/
```

Make it executable:
```bash
chmod +x .git/hooks/pre-commit
```

## Troubleshooting

### Python not found
- Ensure Python 3.8+ is installed
- Use `python3` instead of `python` on Linux/Mac

### Module import errors
- Ensure you're in the virtual environment
- Check that you're running from the project root directory

### Test failures
- Verify all dependencies are installed
- Check Python version compatibility
- Review test output for specific errors

## Next Steps

1. Explore the data structures and algorithms
2. Run the existing implementations
3. Try the practice problems
4. Contribute your own solutions!
