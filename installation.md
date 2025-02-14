
1️⃣ Clone the Repository
```
git clone https://github.com/kathy20316/EducationOrder
cd EducationOrder
```

2️⃣ Set Up Backend (Django)

Create a virtual environment and install dependencies:
```
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
pip install -r requirements.txt
```

Run database migrations:
```
python manage.py migrate
```

Start the Django development server:
```
python manage.py runserver
```

3️⃣ Set Up Frontend (React)

Navigate to the frontend directory and install dependencies:
```
cd frontend
npm install
```

Start the React development server:
```
npm start
```

4️⃣ Running Tests

Run Django tests:
```
python manage.py test
```

Run React tests:
```
npm test
```

5️⃣ Deployment

The project uses GitHub Actions for CI/CD.
Push to main or develop branches to trigger deployment workflows.​​
