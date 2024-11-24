# initial_project_name

A wee python project

## Setup
```bash
poetry install
```

## Usage
Run the main script:
```bash
poetry run run
```

## Adding dependencies
```bash
poetry add <package>
```

## Common Poetry Commands

### Development
```bash
# Install dependencies
poetry install

# Add a new dependency
poetry add <package>

# Add a development dependency
poetry add --group dev <package>

# Remove a dependency
poetry remove <package>

# Update dependencies
poetry update

# Show currently installed dependencies
poetry show

# Activate virtual environment
poetry shell
```

### Testing & Linting
```bash
# Run tests
poetry run pytest

# Run specific test file
poetry run pytest tests/test_file.py

# Run linting
poetry run flake8
poetry run black .
```

### Project Management
```bash
# Create a new project
poetry new project_name

# Build project
poetry build

# Publish to PyPI
poetry publish

# Export requirements.txt
poetry export -f requirements.txt --output requirements.txt
```

## Development Setup

### Pre-commit Hooks (recommended)
```bash
# Install pre-commit
poetry add --group dev pre-commit

# Install git hooks
pre-commit install
```

## Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License
[MIT](LICENSE)

