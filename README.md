
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

## Installation Guide

### Prerequisites

Before installing Enhanced Agent Zero, ensure you have the following installed on your system:

- **Python 3.9 or higher**
- **pip** (Python package installer, usually included with Python)
- **Git** (Version control system)

---

### Option 1: Docker (Recommended)

The recommended way to run the Enhanced Agent Zero is to build and run it from this specific GitHub repository.

1.  **Install Docker**:
    - **Linux**: Follow the instructions for your distribution (e.g., `sudo apt-get install docker.io`).
    - **Mac**: Download and install [Docker Desktop](https://www.docker.com/products/docker-desktop/).

2.  **Clone the repository**:
    ```bash
    git clone https://github.com/vaibhavmaurya20/Enhanced-Agentzero.git
    cd Enhanced-Agentzero
    ```

3.  **Build the Docker image**:
    ```bash
    docker build -t enhanced-agent-zero -f docker/run/Dockerfile .
    ```

4.  **Run the container**:
    ```bash
    docker run -p 50001:80 -v $(pwd)/data:/a0/usr enhanced-agent-zero
    ```

5.  **Access the Interface**:
    Open your browser and go to `http://localhost:50001`.

---

### Option 2: Installation on Linux (Step-by-Step)

Follow these steps to set up and run Enhanced Agent Zero directly on Linux.

1.  **Open your terminal**.

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

5.  **Upgrade pip** (Optional but recommended):
    ```bash
    pip install --upgrade pip
    ```

6.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

7.  **Run Enhanced Agent Zero**:
    ```bash
    python run_ui.py
    ```

8.  **Access the Interface**:
    Open your web browser and navigate to `http://localhost:5000`.

---

### Option 3: Installation on macOS (Step-by-Step)

Follow these steps for macOS setup. If you do not have Homebrew installed, it is the easiest way to manage packages.

1.  **Install Homebrew** (if not already installed):
    Run the install command from [brew.sh](https://brew.sh/).

2.  **Install Python 3 and Git**:
    ```bash
    brew install python3 git
    ```

3.  **Clone the repository**:
    ```bash
    git clone https://github.com/vaibhavmaurya20/Enhanced-Agentzero.git
    cd Enhanced-Agentzero
    ```

4.  **Create a virtual environment**:
    ```bash
    python3 -m venv venv
    ```

5.  **Activate the virtual environment**:
    ```bash
    source venv/bin/activate
    ```

6.  **Upgrade pip**:
    ```bash
    pip install --upgrade pip
    ```

7.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

8.  **Run Enhanced Agent Zero**:
    ```bash
    python run_ui.py
    ```

9.  **Access the Interface**:
    Open your web browser and go to the address shown in your terminal.

---

## Configuration

After launching the agent, open the Web UI. You will need to configure your AI Provider API keys (e.g., OpenAI, Anthropic, Groq) in the "Settings" section to enable full functionality.

## Troubleshooting

- **Port Already in Use**: If you encounter an error about port 5000 (Linux/Mac) or 50001 (Docker) being in use, the framework will automatically try the next available port.
- **Permission Denied**: Ensure you have write permissions for the folder where you cloned the repository.
- **Dependencies Fail**: Ensure `python3`, `pip`, and `git` are correctly installed and up to date.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
