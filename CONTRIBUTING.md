# Contributing to DSA Mastery

Thank you for your interest in contributing to this project! Here's how you can help:

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/YOUR_USERNAME/dsa-mastery-.git`
3. Create a new branch: `git checkout -b feature/your-feature-name`
4. Make your changes
5. Commit with clear messages: `git commit -m "Add: description of changes"`
6. Push to your fork: `git push origin feature/your-feature-name`
7. Open a Pull Request

## Code Style Guidelines

- Follow PEP 8 Python style guidelines
- Add docstrings to all functions and classes
- Include type hints where applicable
- Write clear, descriptive variable names
- Keep functions focused and modular

## Example Format for Contributions

```python
def algorithm_name(input_param: list) -> int:
    """
    Brief description of what the algorithm does.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Args:
        input_param: Description of the parameter
        
    Returns:
        Description of return value
        
    Example:
        >>> algorithm_name([1, 2, 3])
        6
    """
    # Implementation here
    pass
```

## What to Contribute

- ✅ New algorithm implementations
- ✅ Bug fixes and improvements
- ✅ Better explanations and comments
- ✅ Additional test cases
- ✅ Optimized solutions
- ✅ Documentation improvements
- ✅ Practice problems with solutions

## Quality Checklist

Before submitting a PR, ensure:

- [ ] Code follows PEP 8 style guidelines
- [ ] Functions have docstrings with complexity analysis
- [ ] Type hints are included
- [ ] Examples are provided
- [ ] No hardcoded test values
- [ ] Comments explain the "why", not the "what"
- [ ] Code is tested and works correctly

## Testing

Include test cases with your submissions:

```python
def test_algorithm_name():
    assert algorithm_name([1, 2, 3]) == expected_output
    assert algorithm_name([]) == expected_output
    assert algorithm_name([1]) == expected_output
```

## Naming Conventions

- **Files**: Use snake_case (e.g., `bubble_sort.py`)
- **Functions**: Use snake_case (e.g., `bubble_sort()`)
- **Classes**: Use PascalCase (e.g., `LinkedListNode`)
- **Constants**: Use UPPER_SNAKE_CASE (e.g., `MAX_SIZE`)

## Report Issues

Found a bug or have suggestions? Open an issue with:
- Clear description of the problem
- Steps to reproduce
- Expected vs actual behavior
- Python version and environment info

## Questions?

Feel free to ask questions in issues or discussions. We're here to help!

Happy Contributing! 🚀
