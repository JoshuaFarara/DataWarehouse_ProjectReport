# def generate_roll_up_query(selected_dimension, selected_footsteps):
#     # Constructing the SELECT clause for the query
#     select_clause = ", ".join(selected_footsteps + ["COUNT(*) as num_of_graduates"])

#     # Constructing the GROUP BY clause for the query
#     group_by_clause = ", ".join(selected_footsteps + ["ROLLUP({})".format(", ".join(selected_footsteps))])

#     #constructing the JOIN clauses
#     join_clause = None

#     #constructing the where clause
#     where_clause = None

#     # Constructing the SQL query
#     sql_query = f"""
#         SELECT {select_clause}
#         FROM fact_table f
#         GROUP BY {group_by_clause}
#     """

#     return sql_query

# # Example data for OLAP operation
# olap_data = {
#     "selectedOLAP": "Roll Up",
#     "selected_dimension": "dim_degrees",
#     "selected_footsteps": [
#         "major_name",
#         "degree_depth"
#     ]
# }

# # Extracting data from OLAP operation information
# selected_dimension = olap_data["selected_dimension"]
# selected_footsteps = olap_data["selected_footsteps"]

# # Generating SQL query for Roll Up operation
# sql_query = generate_roll_up_query(selected_dimension, selected_footsteps)
# print(sql_query)  # Replace with your database connection and execution

def generate_sql_query(selected_dimensions, selected_footsteps, selected_filters):
    # Constructing the SELECT clause for the query
    # select_clause = ", ".join(selected_footsteps + ["COUNT(*) as num_of_graduates"])
    select_clause = "COUNT(*) as num_of_graduates"

    # Constructing the FROM clause with aliases for the fact table and dimensions
    fact_table_alias = "f"
    from_clause = f"FROM fact_table {fact_table_alias}"
    join_clauses = []

    dimension_ids = {'dim_degrees':'degree_id', 
                         'dim_time':'time_id',
                         'dim_gparank':'gparank_id',
                         'dim_status':'status_id' 
        }
    # Constructing the JOIN clauses for selected dimensions with aliases
    for dimension in selected_dimensions:
        dim_alias = f"{dimension[4:7]}"  # Create a 3-letter alias for the dimension table
        dimension_id_key = f"{dimension}"  # Generating the dimension_id key

        # join_clause = f"""
        #     JOIN {dimension} {dim_alias}
        #     ON {fact_table_alias}.{dimension}_id = {dim_alias}.{dimension}_id
        # """
        if dimension_id_key in dimension_ids:  # Checking if the dimension_id exists in the dictionary
            join_clause = f"""
                JOIN {dimension} {dim_alias}
                ON {fact_table_alias}.{dimension_ids[dimension_id_key]} = {dim_alias}.{dimension_ids[dimension_id_key]}
            """
        # join_clauses.append(join_clause)
            join_clauses.append(join_clause)

    full_join_clause = '\n'.join(join_clauses)
    
    
    # Constructing the WHERE clause for selected filters
    where_conditions = []
    for filter_name, filter_value in selected_filters.items():
        where_conditions.append(f"{fact_table_alias}.{filter_name} = '{filter_value}'")

    

    # Constructing the SQL query with appropriate JOINs and WHERE conditions
    # {' '.join(join_clauses)} # can be reinserted below {from_clause}
    sql_query = f"""
        SELECT {select_clause}
        {from_clause}
        {full_join_clause}
        WHERE {' AND '.join(where_conditions)}
        
    """
    # GROUP BY {", ".join(selected_footsteps)} can be added to query if needed

    return sql_query

# Example data for OLAP operation
olap_data = {
    "selectedOLAP": "Roll Up",
    "selected_dimensions": ["dim_degrees", "dim_time"],
    "selected_footsteps": ["major_name", "year"],
    "selected_filters": {
        "year": 1988,
        "semester_name": "Spring",
        "major_name": "Computer Sc",
        # Add more filters based on the HTML form dropdowns
    }
}

# Extracting data from OLAP operation information
selected_dimensions = olap_data["selected_dimensions"]
selected_footsteps = olap_data["selected_footsteps"]
selected_filters = olap_data["selected_filters"]

# Generating SQL query for Roll Up operation
sql_query = generate_sql_query(selected_dimensions, selected_footsteps, selected_filters)
print(sql_query)  # Replace with your database connection and execution
