# G-App Suite Password Generator

## Overview
The G-App Suite Password Generator is a secure and customizable tool designed to generate strong passwords within the G-App Suite ecosystem. This repository contains the source code and resources for the Password Generator application.

## Features
- **Customizable Passwords**: Generate passwords with configurable length, including letters, numbers, and special characters.
- **Clipboard Support**: Easily copy generated passwords to the clipboard.
- **Cross-Platform**: Runs on Windows, macOS, and Linux.

## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/gunungpw/gapp-passgen.git
   ```
2. **Navigate to the Project Directory**:
   ```bash
   cd gapp-passgen
   ```
3. **Install UV**:
   Install `uv` using the official installation method. Follow the instructions for your operating system from the [official UV documentation](https://docs.astral.sh/uv/getting-started/installation/). For example, on Unix-based systems (Linux/macOS):
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```
   For Windows, use PowerShell:
   ```bash
   powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
   ```
4. **Install Dependencies**:
   Use `uv` to install dependencies defined in `pyproject.toml`. This will create a virtual environment and install the required packages.
   ```bash
   uv sync
   ```
5. **Run the Application**:
   Activate the virtual environment and run the application:
   ```bash
   uv run python src/main.py
   ```

## Usage
- Launch the application to access the password generation interface.
- Adjust settings such as password length and character types (uppercase, lowercase, numbers, symbols).
- Generate a password and copy it to the clipboard for immediate use.

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a Pull Request.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact
For questions or support, please open an issue on the [GitHub Issues page](https://github.com/gunungpw/gapp-passgen/issues) or contact the maintainer at gunungpambudiw@gmail.com.

---

&copy; 2025 Gunung Pambudi Wibisono. All rights reserved.
