# WeatherApp - A Kubernetes-based Weather Forecasting Application

This is a simple weather forecasting application built using Python and Flask. The application fetches real-time weather data from OpenWeatherMap API, displays it to the user, and is containerized using Docker. The application is deployed and orchestrated with Kubernetes for scaling and management.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Setting up the Environment](#setting-up-the-environment)
- [WeatherApp Backend](#weatherapp-backend)
  - [Step 1: Write the Python Script](#step-1-write-the-python-script)
  - [Step 2: Handle API Key Securely](#step-2-handle-api-key-securely)
  - [Step 3: Handle Errors Gracefully](#step-3-handle-errors-gracefully)
  - [Step 4: Testing](#step-4-testing)
- [Docker Setup](#docker-setup)
  - [Dockerfile](#dockerfile)
  - [Building Docker Image](#building-docker-image)
  - [Running Docker Container](#running-docker-container)
- [Kubernetes Setup](#kubernetes-setup)
  - [Create a Kubernetes Cluster with KIND](#create-a-kubernetes-cluster-with-kind)
  - [Deploy to Kubernetes](#deploy-to-kubernetes)
  - [Access the Application](#access-the-application)
- [License](#license)

## Overview

This project is a weather application that interacts with the OpenWeatherMap API to fetch real-time weather information. The application is designed to be containerized using Docker and deployed on a Kubernetes cluster for scalability. The backend is built with Python and Flask.

## Features
- Fetches real-time weather data from the OpenWeatherMap API.
- Displays the current temperature, weather description, humidity, and wind speed.
- Containerized backend with Docker.
- Deployed on Kubernetes for scalability and orchestration.

## Technologies Used
- **Python** (Flask)
- **Docker**
- **Kubernetes**
- **OpenWeatherMap API**
- **Kubernetes In Docker** (KIND)

## Getting Started

### Prerequisites
To run this application locally, you'll need to have the following installed:
- **Python 3.x**: The backend is written in Python.
- **Docker**: For containerizing the application.
- **Kubernetes**: For orchestration (via KIND or Minikube for local clusters).
- **kubectl**: The command-line tool for interacting with Kubernetes.
- **API Key**: You’ll need a valid API key from [OpenWeatherMap](https://openweathermap.org/api) to fetch weather data.

### Installation

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/meghapatel250/WeatherApp.git
   cd WeatherApp/backend
