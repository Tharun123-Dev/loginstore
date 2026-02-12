
🚆 IRCTC Booking Portal (Full Stack Project)
📌 Project Overview

This is a Full Stack IRCTC-style Railway Booking Portal built using:

Backend: Django

Frontend: Vite + React

Database: MySQL (Aiven compatible)

Authentication: Django Session Authentication

Admin Panel: Django Admin

The project allows:

Users to register and login

Users to view personalized dashboard

Users to search available trains

Admin to add/manage trains via admin panel

Users to view trains added by admin
🏗️ Project Architecture
Frontend (Vite + React)
        ↓
Axios API Calls
        ↓
Django Backend
        ↓
MySQL Database
        ↓
Django Admin Panel

🔐 Authentication Flow

User Signup

User Login

Django creates session

Session stored in browser cookie

Protected APIs check authentication

User Dashboard opens

Session-based authentication is implemented using Django's built-in authenticate() and login() functions.

👤 User Features
✅ 1. Signup

Username validation

Email format validation

Password length validation

Duplicate username & email check

✅ 2. Login

Field validation

Proper status codes

Session creation

Secure authentication

✅ 3. Dashboard

After successful login, user sees:

Welcome message with username

User email

IRCTC Dashboard section

Search Trains feature

🚆 Train Search Feature

Users can:

Enter source

Enter destination

Search train

Results display:

Train Number

Train Name

Source

Destination

Departure Time

Arrival Time

🛠️ Admin Features

Admin can:

Login via Django Admin Panel

Add new trains

Update trains

Delete trains

Filter & search trains

Admin URL:http://127:0:0.1:8000/admin/🔒 Middleware Used

Custom middleware implemented for:

Request logging

API route protection

Validation handling

🎨 Frontend Technologies

React (Vite)

useState

useEffect

Axios for API calls

Session-based authentication handling

🚀 How to Run the Project
Backend Setup

pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

Frontend Setup
npm install
npm run dev
📊 Project Workflow

Admin logs in and adds trains.

User signs up and logs in.

User opens dashboard.

User searches trains.

Trains added by admin are visible to user.
🚀 Future Enhancements (Features to be Implemented)

The following features are planned for future development:

🎟 1. Ticket Booking System

Seat availability logic

Class selection (Sleeper, AC, 2A, 3A)

Passenger details form

Ticket confirmation page

PNR generation

💳 2. Payment Integration

Debit / Credit Card simulation

UPI payment simulation

Save payment methods

Payment success / failure handling

Transaction history

📋 3. Booking History

View previous bookings

Download ticket (PDF)

Cancel ticket option

Refund simulation

👥 4. Passenger Management

Save frequent passengers

Edit passenger details

Delete passenger records

Auto-fill during booking

🔐 5. Role-Based Access Control

Admin dashboard (separate UI)

Staff management system

Role-based middleware

Permission-based route protection

📊 6. Dashboard Improvements

Booking statistics

Upcoming journey section

Notifications panel

Recent search history

🧾 7. Advanced Train Search

Date-based filtering

Seat availability display

Price calculation

Sort by departure time

🌍 8. Deployment & Production Enhancements

Deploy backend on cloud (Render/Railway)

Deploy frontend on Vercel

Environment variable management

HTTPS security setup

🔄 9. JWT Authentication Version

Token-based authentication

Refresh token system

Secure API authorization

Production-ready security

📱 10. UI Improvements

Responsive mobile design

Improved UI/UX

Modern dashboard layout



