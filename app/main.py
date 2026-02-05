from fastapi import FastAPI
from . import dal
import json
from .json_to_mongo import main

app = FastAPI()

@app.post("/seed_database")
def add_data():
    main()

@app.get("/employees/engineering/high-salary")
def get_high_salary():
    
    results = dal.get_engineering_high_salary_employees()
    
    return results

@app.get('/employees/by-age-and-role')
def get_age_role():
    results = dal.get_employees_by_age_and_role()
    return results

@app.get('/employees/top-seniority')
def get_senior():
    results = dal.get_top_seniority_employees_excluding_hr()
    return results
@app.get('/employees/age-or-seniority')
def get_age_senior():
    results = dal.get_employees_by_age_or_seniority()
    return results
@app.get('/employees/managers/excluding-departments')
def get_managers():
    results = dal.get_managers_excluding_departments()
    return results

@app.get('/employees/by-lastname-and-age')
def get_last():
    results = dal.get_employees_by_lastname_and_age()
    return results