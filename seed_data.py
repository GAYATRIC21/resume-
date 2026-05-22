import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'resume_project.settings')
django.setup()

from portfolio.models import Skill, Project, ProjectBullet, Experience, ExperienceBullet, Education

# Clear existing
Skill.objects.all().delete()
Project.objects.all().delete()
Experience.objects.all().delete()
Education.objects.all().delete()

# Skills
skills_data = [
    ('Python', 'languages', 1), ('JavaScript', 'languages', 2), ('TypeScript', 'languages', 3),
    ('Java', 'languages', 4), ('C/C++', 'languages', 5), ('SQL', 'languages', 6),
    ('React.js', 'frameworks', 1), ('Angular', 'frameworks', 2), ('Node.js', 'frameworks', 3),
    ('Django', 'frameworks', 4), ('Bootstrap', 'frameworks', 5), ('Pandas', 'frameworks', 6),
    ('NumPy', 'frameworks', 7), ('scikit-learn', 'frameworks', 8),
    ('AWS', 'cloud_db', 1), ('Azure', 'cloud_db', 2), ('MySQL', 'cloud_db', 3),
    ('MongoDB', 'cloud_db', 4), ('SQLite', 'cloud_db', 5),
    ('Git/GitHub', 'tools', 1), ('VS Code', 'tools', 2), ('PyCharm', 'tools', 3),
    ('Android Studio', 'tools', 4), ('Postman', 'tools', 5),
    ('REST APIs', 'concepts', 1), ('MVVM Architecture', 'concepts', 2),
    ('SDLC', 'concepts', 3), ('Agile', 'concepts', 4), ('OOP', 'concepts', 5),
    ('Data Structures & Algorithms', 'concepts', 6),
]
for name, cat, order in skills_data:
    Skill.objects.create(name=name, category=cat, order=order)

# Projects
p1 = Project.objects.create(
    title='Blood Bank Management System',
    description='A secure Django web application that digitizes blood donation workflows end-to-end.',
    tech_stack='Django · Python · MySQL · Bootstrap',
    github_url='https://github.com/GAYATRIC21/blood-bank-management',
    start_date='Jan 2026', end_date='May 2026',
    featured=True, order=1
)
for i, text in enumerate([
    'Built a secure web application to digitize blood donation workflows, cutting manual record-keeping errors by 90% across 8+ blood types.',
    'Implemented real-time inventory tracking enabling instant blood availability checks for hospital staff and administrators.',
    'Developed full CRUD functionality for donor registration, blood request processing, and admin-approved donation history.',
    'Deployed with role-based access control differentiating donor, hospital, and admin users for data security.',
], 1):
    ProjectBullet.objects.create(project=p1, text=text, order=i)

p2 = Project.objects.create(
    title='Responsive Restaurant Website',
    description='A mobile-first restaurant website with interactive menu and reservation system.',
    tech_stack='HTML5 · CSS3 · JavaScript · React',
    github_url='https://github.com/GAYATRIC21/restaurant-website',
    start_date='Apr 2023', end_date='May 2023',
    featured=False, order=2
)
for i, text in enumerate([
    'Designed and built a mobile-first restaurant website with interactive menu, online reservation form, and photo gallery.',
    'Implemented responsive layout using CSS Grid and Flexbox ensuring cross-browser compatibility across Chrome, Firefox, and Safari.',
    'Integrated form validation and smooth-scroll UX patterns to improve customer engagement and drive reservations.',
], 1):
    ProjectBullet.objects.create(project=p2, text=text, order=i)

# Experience
e1 = Experience.objects.create(
    role='Web Developer Intern', company='PHN Technology',
    location='Pune, Maharashtra', start_date='Apr 2023', end_date='Jun 2023', order=1
)
for i, text in enumerate([
    'Developed and maintained responsive UIs using HTML5, CSS3, and JavaScript (ES6+), ensuring cross-browser compatibility and mobile-first design.',
    'Built and integrated front-end features with React.js, optimizing component rendering to reduce page load times by 15%.',
    'Identified and resolved front-end bugs alongside the QA team, improving site reliability and reducing reported errors.',
    'Managed code via Git/GitHub within an Agile workflow, participating in daily standups, sprint planning, and code reviews.',
], 1):
    ExperienceBullet.objects.create(experience=e1, text=text, order=i)

e2 = Experience.objects.create(
    role='Android Development Trainee', company='Mountreach Solution Pvt. Ltd.',
    location='Remote', start_date='Aug 2021', end_date='Sep 2021', order=2
)
for i, text in enumerate([
    'Completed hands-on curriculum covering Kotlin and Java for Android, including Activities, Fragments, and Material Design UI patterns.',
    'Consumed RESTful APIs using Retrofit, handled JSON data, and integrated async networking libraries in training projects.',
    'Implemented local data persistence using SQLite/Room Persistence Library following MVVM/LiveData architecture.',
    'Built and tested Android projects including unit testing with JUnit and UI testing with Espresso.',
], 1):
    ExperienceBullet.objects.create(experience=e2, text=text, order=i)

e3 = Experience.objects.create(
    role='Python Programming Trainee', company='Besant Technology',
    location='Chennai, Tamil Nadu', start_date='Apr 2023', end_date='May 2023', order=3
)
for i, text in enumerate([
    'Covered core Python concepts: data types, control structures, OOP principles, and file I/O operations.',
    'Applied NumPy and Pandas for data manipulation tasks including cleaning, aggregation, and basic analysis.',
    'Completed multiple hands-on projects focused on clean, well-documented, and efficient Python code.',
], 1):
    ExperienceBullet.objects.create(experience=e3, text=text, order=i)

# Education
Education.objects.create(
    degree='B.E. in Computer Science and Engineering',
    institution='Siddhivinayak Technical Campus',
    location='Shegao, Maharashtra',
    gpa='7.0 / 10',
    start_date='Aug 2023', end_date='Jun 2026 (Expected)',
    coursework='Data Structures & Algorithms, OOP, Databases, OS, Computer Networks, Machine Learning, Data Mining, Image Processing, Information Retrieval',
    order=1
)
Education.objects.create(
    degree='Diploma in Computer Engineering',
    institution='Government Polytechnic',
    location='Murtizapur, Maharashtra',
    gpa='7.7 / 10',
    start_date='Aug 2019', end_date='Jun 2022',
    coursework='C Programming, Java, Python, Data Structures, DBMS, Computer Networking, Cyber Security, Digital Electronics',
    order=2
)

print("✅ Database seeded successfully!")
