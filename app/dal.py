from connection import Collection 

def get_engineering_high_salary_employees():
    results = Collection.find({
                               "salary": {"$gt": 65000},
                               "job_role.department": "Engineering"
    },
    {"employee_id":1,"name":1, "salary":1})
    return results

def get_employees_by_age_and_role():
    results = Collection.find({
         "$and":[
         {"$and": [
            
            {"age":{"$gte": 30}},
            {"age":{"$lte": 45}}
            
        ]},
        {"$or":[{"job_role.title":"Engineer"},
               {"job_role.title":"Specialist"}
               ]}
               ]
    })
    return results

def get_top_seniority_employees_excluding_hr():
    results = Collection.find({"$nor":[{
        "job_role.department": "HR"}]
    }).sort({"years_at_company":-1}).limit(7)
    return results

def get_employees_by_age_or_seniority():
    results = Collection.find({
        "$or":[
            {"age":{"$gt":50}},
            {"years_at_company": {"$lt": 3}}
        ]
    },{"employee_id":1,"name":1,"age":1,"years_at_company":1 })
    return results

def get_managers_excluding_departments():
    results = Collection.find({"$and":[
        {"job_role.title": "Manager"},
        {
            "$nor": [
                {"job_role.department": "Sales"},
                {"job_role.department": "Marketing"}
            ]
        }
    ]
    })

    return results

def get_employees_by_lastname_and_age():
    results = Collection.find({"$and":[{"$or":
                               [{"name": {"$regex":" Nelson"}},
                                {"name": {"$regex":" Wright"}}
                                ]},
                                {"age":{"$lt": 35}}]},
                              {"name":1,"age":1,"job_role.department":1})
    return results

if __name__ == "__main__":
    results = get_employees_by_lastname_and_age()
    for i in results:
        print(i)
    