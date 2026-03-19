#!/bin/bash

echo "🚀 Building Smart CPMS Project..."

# Step 1: Install dependencies
python3.9 -m pip install -r requirements.txt

# Step 2: Clear old static files and collect new ones
echo "📁 Collecting Static Files..."
python3.9 manage.py collectstatic --noinput --clear

# Step 3: Run database migrations
echo "⚙️ Running Database Migrations..."
python3.9 manage.py migrate --noinput

echo "✅ Build Completed Successfully!"
