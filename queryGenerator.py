def generate_roll_up_query(selected_dimension, selected_footsteps):
    # Constructing the SELECT clause for the query
    select_clause = ", ".join(selected_footsteps + ["COUNT(*) as count_of_degrees"])

    # Constructing the GROUP BY clause for the query
    group_by_clause = ", ".join(selected_footsteps + ["ROLLUP({})".format(", ".join(selected_footsteps))])

    # Constructing the SQL query
    sql_query = f"""
        SELECT {select_clause}
        FROM your_table_name
        GROUP BY {group_by_clause}
    """

    return sql_query

# Example data for OLAP operation
olap_data = {
    "selectedOLAP": "Roll Up",
    "selected_dimension": "dim_degrees",
    "selected_footsteps": [
        "major_name",
        "degree_depth"
    ]
}

# Extracting data from OLAP operation information
selected_dimension = olap_data["selected_dimension"]
selected_footsteps = olap_data["selected_footsteps"]

# Generating SQL query for Roll Up operation
sql_query = generate_roll_up_query(selected_dimension, selected_footsteps)
print(sql_query)  # Replace with your database connection and execution
