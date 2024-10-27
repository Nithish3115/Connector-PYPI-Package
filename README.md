 
🚀 Advanced Python Project Setup with GitHub Actions & MongoDB

This project automates MongoDB operations while optimizing dependency management and testing workflows for Python. With dedicated files for production and development dependencies, robust automated and manual testing setups, and advanced configuration management using pyproject.toml and setup.cfg, this project is ready for any Python development environment.


📋 Overview

Purpose: This project uses GitHub Actions and MongoDB for automated database operations, optimized with a highly modular Python development and testing environment. Our setup includes the following:


Automated MongoDB Operations: Automate data insertion, deletion, and database management.

Structured Dependency Management: Separate dependencies for production and development/testing for easier setup.

Comprehensive Testing Suite: Multiple testing modes, types, and frameworks ensure code quality.

Enhanced Configuration Management: Using pyproject.toml and setup.cfg for streamlined setup and packaging.

📂 Project Structure

bash

 

/project-root

├── src/                         # Core project source code

├── tests/                # Test files and suites

├── .github/workflows/    # GitHub Actions workflows

├── requirements.txt      # Production dependencies

├── requirements_dev.txt  # Development and testing dependencies

├── tox.ini               # Configuration for Tox virtual environments

├── pyproject.toml        # Build system configuration

└── setup.cfg             # Packaging and installation configuration


🛠️ Tech Stack and Dependencies :

Production Dependencies
pymongo[srv]: MongoDB client for Python, necessary for database interactions
dnspython: Provides DNS capabilities for MongoDB connections
Development & Testing Dependencies

Dependencies in requirements_dev.txt are optimized for development and testing:

pandas & numpy: For data manipulation and handling
pytest, tox, tox-gh-actions: Testing frameworks and CI/CD compatibility
pylint, flake8: Code style, formatting, and syntax checking tools for clean and readable code

🔧 Configuration & Setup

pyproject.toml
Defines the configuration for the project’s build system, specifying details like:


Build Tool: Specifies the packaging tool, making it an alternative to setup.cfg
Metadata: Defines package name, version, author, license, and production dependencies

setup.cfg
Primarily used by setuptools for packaging and installing, setup.cfg contains configurations related to packaging, versioning, and dependency management.

🔄 Testing and Virtual Environments:
 
This project supports a comprehensive suite of tests, as well as automated and manual testing modes.

Types of Testing

Unit Testing: Individual module-level tests to ensure each part functions correctly.

Integration Testing: Tests that check interactions between components.

Code Style & Syntax Checks: Tools to ensure consistent coding standards:

pylint

flake8 (bundles pylint, pycodestyle, and mccabe)

Testing Frameworks :

pytest: Primary testing framework

unittest: Standard library for basic tests 

robotframework: Supports automated acceptance testing

selenium, behave, doctest: For specialized testing needs

Running Tests

Use tox to test the project across multiple environments and Python versions:


 
tox

Local Testing with GitHub Actions

For local and remote testing compatibility with GitHub Actions, configure workflows to cover tests against various Python versions.

🎯 Usage :

This project is designed to be easy to use and maintain, with commands for automation, testing, and virtual environment setup.

Key Commands

Setting up a Virtual Environment: Use tox to create isolated environments for testing against different Python versions and dependency configurations.
Run Tests: pytest for quick, direct testing:
 
🤝 Contributing
Contributions are welcome! Please follow these steps:

Fork this repository.

Create a branch: git checkout -b feature-branch.

Make changes, commit, and push.

Submit a pull request for review!

📄 License

This project is licensed under the MIT License.## Color Reference

 
## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`API_KEY`

`ANOTHER_API_KEY` 

 
## API Reference

#### Get all items

```http
  GET /api/items
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. Your API key |

#### Get item

```http
  GET /api/items/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |

 

 

