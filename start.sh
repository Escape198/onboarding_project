#!/bin/bash

echo "Starting backend server..."
cd backend || exit
uvicorn app.main:app --reload &

echo "Starting frontend server..."
cd ../frontend || exit
python3 -m http.server 8080