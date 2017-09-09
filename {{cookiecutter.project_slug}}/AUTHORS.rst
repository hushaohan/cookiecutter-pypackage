* {{ cookiecutter.full_name }} {% if cookiecutter.project_type == 'Personal' -%}
 <{{ cookiecutter.personal_email }}>
{%- elif cookiecutter.project_type == 'Work' -%}
 <{{ cookiecutter.work_email }}>
{%- endif -%}
