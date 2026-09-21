# Air Quality Prediction - MLOps

## Project Overview

This project predicts the **US Air Quality Index (US AQI)** using pollutant measurements with a Machine Learning model.

The project also demonstrates an MLOps workflow by deploying the trained model as a FastAPI application and preparing it for cloud deployment using Render.

## Machine Learning Model

The project uses **Multiple Linear Regression**.

### Input Features

- PM2.5
- PM10
- Carbon Monoxide
- Nitrogen Dioxide
- Sulphur Dioxide
- Ozone

### Target

- US AQI

## Model Evaluation

The model was evaluated using:

- Mean Squared Error (MSE): 65.96
- R² Score: 0.53
- RMSE: approximately 8.12

The model was trained using an 80% training and 20% testing split.

## API

The trained model is served using **FastAPI**.

### Prediction Endpoint

```text
POST /predict
