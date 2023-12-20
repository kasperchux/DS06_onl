
CREATE TABLE IF NOT EXISTS employees (
    employee_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    salary NUMERIC(10, 2) NOT NULL
);

CREATE TABLE IF NOT EXISTS departments (
    department_id SERIAL PRIMARY KEY,
    department_name VARCHAR(50) NOT NULL
);

INSERT INTO employees (first_name, last_name, salary) VALUES
    ('John', 'Doe', 50000),
    ('Jane', 'Smith', 60000),
    ('Bob', 'Johnson', 55000);

INSERT INTO departments (department_name) VALUES
    ('IT'),
    ('HR'),
    ('Finance');
    
    
    
    
CREATE OR REPLACE FUNCTION get_employee_info(employee_id INT)
RETURNS TABLE (first_name VARCHAR(50), last_name VARCHAR(50), salary NUMERIC(10, 2))
AS $$
BEGIN
    RETURN QUERY SELECT employees.first_name, employees.last_name, employees.salary
                 FROM employees
                 WHERE employees.employee_id = get_employee_info.employee_id;
END;
$$ LANGUAGE plpgsql;

select get_employee_info(1)