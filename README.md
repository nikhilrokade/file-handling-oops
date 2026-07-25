# Corporate Workforce & Financial Management System (OOP & File Handling)

A production-grade Python application demonstrating advanced **Object-Oriented Programming (OOP)** architectures, enterprise **File I/O operations**, and automated data handling patterns.

---

## 🛠️ Core Engineering Concepts Implemented

*   **Abstraction & Inheritance**: Utilizes the `abc` module to enforce template configurations via `Organisation(ABC)` abstract base classes extended by operational `Employee` classes.
*   **Encapsulation**: Strict use of access modifiers (private double underscores `__` and protected single underscores `_`) to safely sandbox sensitive fields like `salary`.
*   **Polymorphism & Method Overriding**: Dynamic runtime resolution used to alter standard corporate behaviors (e.g., dynamically resolving custom enterprise asset addresses using `headquater()`).
*   **Method Injection & Type Hinting**: Structural dependencies are elegantly solved by injecting complex `Employee` class instances directly inside independent `FinanceManagement` components.
*   **Robust Input Validation**: Embeds Python `re` (Regular Expression) validation frameworks to enforce banking infrastructure rules (`^\d{9,18}$`).

---

## 📁 Repository Architecture

*   `org_emp_oops_python.py`: Houses the foundational enterprise domain architectures, abstraction skeletons, data fields, and operational financial components.
*   `csv_filehandling_oops_python.py`: Manages database transactions, persistence pipelines, and serialized structural exports to `.csv` tables.
*   `driver_main_oops_python.py`: Serves as the centralized project execution controller, handling workflow initialization and state management.

---

## 🚀 Execution & Setup Guide

### 1. Replicate Project Ecosystem
```bash
git clone https://github.com
cd file-handling-oops
```

### 2. Launch Application Pipelines
```bash
python driver_main_oops_python.py
```

---

## 📊 Sample Program Outputs

### Structural Corporate Overview
```text
Organisation Name: ReBIT
Sector Type : Private / Corporate Sector
Governed By : Supervised by Government Laws
Registered ID: 2500

Basic Details of Employees:
Employee Id: 101, Employee Full Name: Nikhil Rokade, Age: 26
Department and Division: Cyber Security
```

### Financial Audit Output
```text
Depositing Amount to Employee ID 101 ---
Printing Deposit Amount: 50000
Successfully deposited: 50000. Current Balance is: 50000
```
