🥦 Food Macros Search Engine (Cloud-Deployed API)
A high-performance, production-ready search API that provides instant macronutrient data using custom-built algorithmic search structures. Originally a CLI tool, this system has been re-engineered as a FastAPI service deployed on AWS EC2 with a focus on high availability, security, and scalability.

🌍 Live Demo: https://www.usda-food-search.com (Swagger UI)

🚀 Key Evolutions
From CLI to API: Migrated a local Python script into a robust FastAPI backend.

High Availability: Implemented a Load Balancing strategy using Nginx to distribute traffic across multiple worker instances (Ports 8000 & 8001).

Production Security: Fully secured with SSL (Certbot/Let's Encrypt) and Nginx Rate Limiting to prevent API abuse.

Performance: Uses a Trie (Prefix Tree) for O(L) search suggestions and an Inverted Index for instant nutrient lookups, bypassing the need for heavy database queries.

🏗️ Architecture & Infrastructure
Reverse Proxy & Load Balancer: Nginx handles SSL termination and uses a least_conn algorithm to balance requests between backend workers.

Process Management: Systemd manages independent API workers, ensuring they auto-restart on failure.

Rate Limiting: Configured at the Nginx level (10r/s) with a burst buffer to protect system resources.

Deployment: Automated via shell scripts for consistent environment builds (virtual environments, dependency injection, and service configuration).

🧠 Algorithmic Core
The engine avoids slow linear scans of the USDA dataset by using optimized data structures:

Trie (Prefix Tree): Powers the autocomplete. It maps prefixes to complete food names in time proportional to the word length (L), not the dataset size (N).

Inverted Index: Maps specific search tokens to unique Food IDs.

Macro Mapping: Instantly retrieves Protein, Carbs, Fats, and Calories from the pre-processed food_macros.csv using the indexed IDs.

📁 Repository Structure
File	Purpose
main.py	FastAPI application and endpoint logic
search_engine.py	Core algorithmic logic (Trie & Indexing)
deploy_nginx.sh	Production: Automates EC2 setup, Nginx config, and SSL
init.sh	Local: Bootstraps the Python environment and dependencies
start.sh	Development: Launches the Uvicorn server with hot-reload
⚙️ Getting Started
Local Development

To run the API on your local machine:

Initialize Environment:

Bash
chmod +x init.sh
./init.sh
Start the Server:

Bash
chmod +x start.sh
./start.sh
Access Docs: Open http://127.0.0.1:8000/docs to test the endpoints via Swagger.

Production Deployment (EC2)

The deploy_nginx.sh script is designed for Ubuntu-based EC2 instances.

Note: Before running, update the DOMAIN and EMAIL variables inside the script to match your public IP/Domain records.

Bash
# Update variables inside script
nano deploy_nginx.sh 

# Execute deployment
sudo chmod +x deploy_nginx.sh
./deploy_nginx.sh
🛠️ Tech Stack
Backend: Python, FastAPI, Uvicorn

Data Science: Pandas, Jupyter (Preprocessing)

Web Server: Nginx (Load Balancer, Reverse Proxy)

Cloud: AWS EC2, Route 53

Security: Certbot (SSL), Nginx Rate Limiting, Systemd
