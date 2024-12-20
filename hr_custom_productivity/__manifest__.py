{
    'name': 'HR Custom Productivity',
    "author": "Basel Mahmoud/ Business Haven Consultants",
    "version": "17.0.1.0",
    "website": "https://www.softhealer.com",
    'category': 'Human Resources',
    'license': 'LGPL-3',
    'summary': 'Dynamic management of production ranges for payroll calculations.',
    'description': """
        This module provides:
        - Automated salary calculations based on productivity ranges.
        - Daily productivity tracking for employees.
        - Configurable rates for different production ranges by department.
        - Enhanced HR reporting with productivity metrics.
        
        Technical Features:
        - Integration with HR Payroll for streamlined calculations.
        - Custom views for managing production ranges.
        - Security controls with group-specific access.
    """,
    'depends': ['base', 'hr', 'hr_payroll_community'],
    "data": [
        'security/ir.model.access.csv',
        'views/production_range_views.xml',
        'views/hr_attendance_inherit_views.xml',
        # 'views/payslip_views.xml',
        # 'views/salary_rule_views.xml',
    ],
    'tags': ['HR', 'Payroll', 'Productivity', 'Automation'],
    "application": True,
    "installable": True,
}
