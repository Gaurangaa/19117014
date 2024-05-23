
def get_input(prompt, default):
    user_input = input(f"{prompt} (default value: {default}): ")
    return float(user_input) if user_input else default

def calculate_costs():
    # User inputs with default values
    number_of_machines = get_input("Number of Machines", 100)
    raspberry_pi_cost = get_input("Raspberry Pi Pico cost ₹", 300)


how to save it in github repsoitory asn add a hyperlink whose name is Implementation of basic framewrok for Cost analysis.
    temp_sensor_cost = get_input("Temperature Sensor (DS18B20) cost ₹", 400)
    vibration_sensor_cost = get_input("Vibration Sensor (SW-420) cost ₹", 150)
    current_sensor_cost = get_input("Current Sensor (ACS712) cost ₹", 250)
    torque_sensor_cost = get_input("Torque Sensor (strain gauge-based) cost ₹", 4000)
    wifi_module_cost = get_input("ESP8266 Wi-Fi Module cost ₹", 200)
    jumper_wires_cost = get_input("Jumper Wires and Breadboard cost ₹", 100)
    resistors_cost = get_input("Resistors (4.7kΩ) cost ₹", 10)
    installation_cost = get_input("Installation Cost per Machine ₹", 2000)
    bulk_installation_discount = get_input("Discount for bulk installation (%)", 25)
    monthly_data_transfer_cost = get_input("Monthly data transfer per machine ₹", 200)
    monthly_fixed_wifi_cost = get_input("Monthly fixed Wi-Fi cost ₹", 1000)
    initial_setup_cost = get_input("Initial Setup Cost ₹", 100000)
    engineer_cost_per_month = get_input("Engineer Cost per Month ₹", 2000)
    sensor_maintenance_cost_per_month = get_input("Sensor Maintenance Cost per Month ₹", 5000)
    miscellaneous_cost_per_month = get_input("Miscellaneous Cost per Month ₹", 1000)
    traditional_maintenance_cost_per_machine_per_month = get_input("Traditional Maintenance Cost per Month per Machine ₹", 250)
    predictive_maintenance_reduction = get_input("Predictive Maintenance Reduction (%)", 17.5) / 100
    monthly_salary_per_maintenance_staff = get_input("Monthly Salary per Maintenance Staff ₹", 30000)
    staff_count_below_50 = get_input("Staff count for <50 machines", 3)
    staff_reduction_below_50 = get_input("Staff reduction (%) for <50 machines", 10) / 100
    staff_count_above_50 = get_input("Staff count for ≥50 machines", 6)
    staff_reduction_above_50 = get_input("Staff reduction (%) for ≥50 machines", 10) / 100

    # Fixed Costs
    hardware_cost_per_machine = (
        raspberry_pi_cost + temp_sensor_cost + vibration_sensor_cost + current_sensor_cost +
        torque_sensor_cost + wifi_module_cost + jumper_wires_cost + resistors_cost
    )
    discounted_installation_cost = installation_cost * (1 - bulk_installation_discount / 100)
    total_fixed_costs = (hardware_cost_per_machine + discounted_installation_cost) * number_of_machines + initial_setup_cost

    # Variable Costs (Annual)
    total_variable_costs_per_month = (monthly_fixed_wifi_cost + engineer_cost_per_month + sensor_maintenance_cost_per_month + miscellaneous_cost_per_month)
    total_variable_costs_per_year = total_variable_costs_per_month * 12

    # Savings Calculation
    traditional_maintenance_cost_per_year = traditional_maintenance_cost_per_machine_per_month * 12 * number_of_machines
    predictive_maintenance_cost_per_year = traditional_maintenance_cost_per_year * (1 - predictive_maintenance_reduction)
    annual_maintenance_savings = traditional_maintenance_cost_per_year - predictive_maintenance_cost_per_year

    # Staff Cost Calculation
    if number_of_machines < 50:
        annual_staff_cost = staff_count_below_50 * monthly_salary_per_maintenance_staff * 12
        reduced_annual_staff_cost = annual_staff_cost * (1 - staff_reduction_below_50)
    else:
        annual_staff_cost = staff_count_above_50 * monthly_salary_per_maintenance_staff * 12
        reduced_annual_staff_cost = annual_staff_cost * (1 - staff_reduction_above_50)
    
    annual_staff_savings = annual_staff_cost - reduced_annual_staff_cost

    # Total Annual Savings
    total_annual_savings = annual_maintenance_savings + annual_staff_savings - total_variable_costs_per_year

    # ROI Calculation
    investment_recovery_time = total_fixed_costs / (total_annual_savings / 12)

    # Display the results
    print("\n--- Cost Analysis and ROI for Predictive Maintenance ---")
    print(f"Number of Machines: {number_of_machines}")
    print(f"Total Fixed Costs: ₹{total_fixed_costs}")
    print(f"Total Variable Costs (Annual): ₹{total_variable_costs_per_year}")
    print(f"Annual Maintenance Savings: ₹{annual_maintenance_savings}")
    print(f"Annual Staff Savings: ₹{annual_staff_savings}")
    print(f"Total Annual Savings: ₹{total_annual_savings}")
    print(f"Investment Recovery Time: {investment_recovery_time:.2f} months")

# Run the cost analysis
calculate_costs()