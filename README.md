
<div align="center">

# `Enhanced Agent Zero`

[![Website](https://img.shields.io/badge/Website-agent--zero.ai-0A192F?style=for-the-badge&logo=vercel&logoColor=white)](https://agent-zero.ai) 
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

<p align="center">
  A highly advanced AI agent framework engineered for complex task execution, autonomous operation, and seamless human-AI collaboration.
</p>

</div>

## Overview

Enhanced Agent Zero extends the core capabilities of the base framework with specialized modules for:

- **Bioinformatics Integration**: Sequence analysis and DNA manipulation using Biopython.
- **Enhanced Memory System**: Hierarchical, fragmented, and versioned memory storage for precise retrieval.
- **Vision Integration**: Advanced image processing and context awareness.
- **Multi-Provider Orchestrator**: Dynamic routing between various AI providers to optimize performance and reliability.
- **Autonomous Operation Engine**: Self-directed planning, execution, and autonomous error handling.
- **Packaging System**: Automated creation of distributable project archives.

---

## Installation

### Prerequisites

- **Python**: 3.9 or higher
- **pip**: Python package manager
- **Git**: Version control system
- **Node.js & npm** (Optional, for full UI features)

### Option 1: Docker (Recommended)

The easiest way to run Enhanced Agent Zero is using Docker.

1.  **Install Docker**:
    - **Linux**: Follow the instructions for your distribution (e.g., `sudo apt-get install docker.io` or via snap).
    - **Mac**: Download [Docker Desktop](https://www.docker.com/products/docker-desktop/).

2.  **Run with Docker**:

    ```bash
    # Pull the latest image
    docker pull agent0ai/agent-zero

    # Run the container
    docker run -p 50001:80 -v $(pwd)/data:/a0/usr agent0ai/agent-zero
    ```

    Access the Web UI at `http://localhost:50001`.

### Option 2: Installation on Linux (Step-by-Step)

Follow these steps to set up the development environment on Linux.

1.  **Open your terminal**.

2.  **Clone the repository**:

    ```bash
    git clone https://github.com/vaibhavmaurya20/Enhanced-Agentzero.git
    cd Enhanced-Agentzero
    ```

3.  **Create a virtual environment** (to isolate dependencies):

    ```bash
    python3 -m venv venv
    ```

4.  **Activate the virtual environment**:

    ```bash
    source venv/bin/activate
    ```

5.  **Upgrade pip** (optional but recommended):

    ```bash
    pip install --upgrade pip
    ```

6.  **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

7.  **Run the Web UI**:

    ```bash
    python run_ui.py
    ```

8.  **Access the Agent**: Open your browser and go to `http://localhost:5000` (or check the terminal for the specific port).

### Option 3: Installation on macOS (Step-by-Step)

Follow these steps for macOS setup.

1.  **Install Python 3**:
    - The easiest way is using Homebrew.
    - If you don't have Homebrew, install it from [brew.sh](https://brew.sh/).
    - Install Python:

    ```bash
    brew install python3
    brew install git
    ```

2.  **Clone the repository**:

    ```bash
    git clone https://github.com/vaibhavmaurya20/Enhanced-Agentzero.git
    cd Enhanced-Agentzero
    ```

3.  **Create a virtual environment**:

    ```bash
    python3 -m venv venv
    ```

4.  **Activate the virtual environment**:

    ```bash
    source venv/bin/activate
    ```

5.  **Upgrade pip**:

    ```bash
    pip install --upgrade pip
    ```

6.  **Install dependencies**:

    **Note**: Some bioinformatics libraries might require system-level tools. You can install them via Homebrew:

    ```bash
    brew install gcc  # Required for some Python packages
    pip install -r requirements.txt
    ```

7.  **Run the Web UI**:

    ```bash
    python run_ui.py
    ```

    Access the interface in your browser at the address shown in the terminal.

---

## Configuration

After launching, you will need to configure your AI Provider API keys (e.g., OpenAI, Anthropic, etc.) in the "Settings" section of the Web UI to enable full functionality.

## Troubleshooting

- **Port Already in Use**: If you get an error about port 5000 being in use, the framework will automatically try the next available port (e.g., 5001).
- **Permission Denied**: Ensure you have permissions to write in the installation directory.
- **Dependencies Fail**: Ensure `python3` and `pip` are correctly installed and up to date.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
